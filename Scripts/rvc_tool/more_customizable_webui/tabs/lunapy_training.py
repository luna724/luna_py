import gradio as gr
import os
import shutil, math
from multiprocessing import cpu_count

from lib.rvc.preprocessing import extract_f0, extract_feature, split
from lib.rvc.train import create_dataset_meta, glob_dataset, train_index, train_model
from modules.ltrain import set_config
from modules import models, utils
from modules.shared import MODELS_DIR, device, half_support
from modules.ui import Tab

SR_DICT = {
    "32k": 32000,
    "40k": 40000,
    "48k": 48000,
}

class Ltrain(Tab):
  def title(self):
    return "Customized Training"
  
  def sort(self):
    return 7
  
  def ui(self, outlet):
    def ltrain(
      model_name,
          version,
          sampling_rate_str,
          f0,
          dataset_glob,
          recursive,
          multiple_speakers,
          speaker_id,
          gpu_id,
          num_cpu_process,
          norm_audio_when_preprocess,
          pitch_extraction_algo,
          batch_size,
          augment,
          augment_from_pretrain,
          augment_path,
          speaker_info_path,
          cache_batch,
          num_epochs,
          save_every_epoch,
          save_wav_with_checkpoint,
          fp16,
          pre_trained_bottom_model_g,
          pre_trained_bottom_model_d,
          run_train_index,
          reduce_index_size,
          maximum_index_size,
          embedder_name,
          embedding_channels,
          embedding_output_layer,
          ignore_cache,
          lr,
          lr_decay,
          seed
    ):
      set_config(lr, lr_decay, seed)
      batch_size = int(batch_size)
      num_epochs = int(num_epochs)
      maximum_index_size = int(maximum_index_size)
      f0 = f0 == "Yes"
      norm_audio_when_preprocess = norm_audio_when_preprocess == "Yes"
      run_train_index = run_train_index == "Yes"
      reduce_index_size = reduce_index_size == "Yes"
      training_dir = os.path.join(MODELS_DIR, "training", "models", model_name)
      gpu_ids = [int(x.strip()) for x in gpu_id.split(",")] if gpu_id else []

      if os.path.exists(training_dir) and ignore_cache:
          shutil.rmtree(training_dir)

      os.makedirs(training_dir, exist_ok=True)

      yield f"Training directory: {training_dir}"

      datasets = glob_dataset(
          dataset_glob,
          speaker_id,
          multiple_speakers=multiple_speakers,
          recursive=recursive,
          training_dir=training_dir,
      )

      if len(datasets) == 0:
          raise Exception("No audio files found")

      yield "Preprocessing..."
      split.preprocess_audio(
          datasets,
          SR_DICT[sampling_rate_str],
          num_cpu_process,
          training_dir,
          norm_audio_when_preprocess,
          os.path.join(
              MODELS_DIR,
              "training",
              "mute",
              "0_gt_wavs",
              f"mute{sampling_rate_str}.wav",
          ),
      )

      if f0:
          yield "Extracting f0..."
          extract_f0.run(training_dir, num_cpu_process, pitch_extraction_algo)

      yield "Extracting features..."

      embedder_filepath, _, embedder_load_from = models.get_embedder(
          embedder_name
      )

      if embedder_load_from == "local":
          embedder_filepath = os.path.join(
              MODELS_DIR, "embeddings", embedder_filepath
          )

      extract_feature.run(
          training_dir,
          embedder_filepath,
          embedder_load_from,
          int(embedding_channels),
          int(embedding_output_layer),
          gpu_ids,
          None if len(gpu_ids) > 1 else device,
      )

      create_dataset_meta(training_dir, f0)

      yield "Training model..."

      print(f"train_all: emb_name: {embedder_name}")

      config = utils.load_config(
          version, training_dir, sampling_rate_str, embedding_channels, fp16
      )
      out_dir = os.path.join(MODELS_DIR, "checkpoints")

      if not augment_from_pretrain:
          augment_path = None
          speaker_info_path = None

      train_model(
          gpu_ids,
          config,
          training_dir,
          model_name,
          out_dir,
          sampling_rate_str,
          f0,
          batch_size,
          augment,
          augment_path,
          speaker_info_path,
          cache_batch,
          num_epochs,
          save_every_epoch,
          save_wav_with_checkpoint,
          pre_trained_bottom_model_g,
          pre_trained_bottom_model_d,
          embedder_name,
          int(embedding_output_layer),
          False,
          None if len(gpu_ids) > 1 else device,
      )

      yield "Training index..."
      if run_train_index:
          if not reduce_index_size:
              maximum_index_size = None
          train_index(
              training_dir,
              model_name,
              out_dir,
              int(embedding_channels),
              num_cpu_process,
              maximum_index_size,
          )

      yield "Training completed"


    with gr.Group():
      with gr.Blocks():
        with gr.Row():
          model_name = gr.Textbox(label="Model Name", placeholder="Model Name")
          dataset_glob = gr.Textbox(label="Dataset Path", placeholder="/content/gdrive/MyDrive/rvc/dataset/name/*.wav")
        with gr.Accordion("Multiple Speaker"):
          multiple_speakers = gr.Checkbox(label="Multiple Speakers", value=False)
          speaker_id = gr.Slider(0, 4, label="Speaker ID", value=0, step=1)
        recursive = gr.Checkbox(label="Recursive", value=True)
        ignore_cache = gr.Checkbox(label="Ignore cache", value=False)
        
      gr.Markdown("")
      with gr.Blocks():
        with gr.Row():
          version = gr.Radio(choices=["v1","v2"],
                            value="v2",label="Model Version")
          target_sr = gr.Radio(choices=["v1","v2"],
                              value="48k",label="Target Sampling rate")
          f0 = gr.Radio(choices=["Yes","No"],value="Yes",label="Use f0")
        with gr.Row():
          embedding_name = gr.Radio(choices=models.EMBEDDINGS_LIST.keys(),
                                    value="contentvec",
                                    label="Phone Embedder")
          embedding_channels = gr.Radio(choices=["256","768"],
                                        value="256",label="Embedding Channels (Input Dim)")
          embedding_output_layer = gr.Radio(
            choices=["9","12"],
            value="12",
            label="Embedding output Layer"
          )
        with gr.Row():
          gpu_id = gr.Textbox(
                            label="GPU ID",
                            value=", ".join([f"{x.index}" for x in utils.get_gpus()]),
                        )
          num_cpu_process = gr.Slider(0, cpu_count(),
                                      step=1,
                                      value=2,
                                      label="Number of CPU processes")
          norm_audio_when_preprocess = gr.Radio(choices=["Yes", "No"],
                                                value="Yes",
                                                label="Normalize Audio")
        with gr.Row():
          pitch_extraction_algo = gr.Radio(
            choices=["dio", "crepe", "mangio-crepe", "harvest"],
            value="crepe",
            label="Pitch Extraction Algorithm"
          )
          
          batch_size = gr.Number(value=32,label="Batch size")
          # batch_count = gr.Number(value=4,label="Batch count")
          num_epochs = gr.Number(value=240,label="Epochs")
          save_every_epoch = gr.Slider(0,100,value=30,step=1,label="Save Every n Epoch")
          
        with gr.Row():
          lr = gr.Number(label="Learning Rate", value=0.0005)
          lr_decay = gr.Number(label="LR Decay", value=0.9998625)
          seed = gr.Number(label="Seed", value=1234)
          
        with gr.Row():
          save_wav_with_checkpoint = gr.Checkbox(value=False,
                                                label="Save wav with Model")
          cache_batch = gr.Checkbox(label="Cache batch", value=True)
          fp16 = gr.Checkbox(label="FP16 Model", value=False, disabled=not half_support)

        with gr.Row():
          lr_decay_function = gr.Dropdown(choices=["multiply", "cosine"], value="COMING SOON..")
          optimizer = gr.Dropdown(choices=["AdamW"],label="Optimizer",value="AdamW")
          
        per_epoch_infer = gr.Slider(0, 100, step=1, label="Infering Every n Epochs")
        with gr.Accordion("Infering Config",open=False):
          infer_transpose = gr.Slider(-20, 20, step=1, label="Transpose (Pitch)")
          infer_target = gr.Textbox(label="Target File", value="/content/gdrive/MyDrive/RVC-input/夜に駆ける ft. 星乃一歌 Vocal.wav")
          
      gr.Markdown("<br>")
      with gr.Blocks():
        with gr.Row():
          augment = gr.Checkbox(label="Augment", value=False)
          augment_from_pretrain = gr.Checkbox(label="Augment From Pretrain",value=False)
          
        with gr.Row():
          augment_path = gr.Textbox(label="Pre trained generator path (pth)",
                                    value="file is not prepared")
          speaker_info_path = gr.Textbox(label="Speaker Info path (npy)",
                                        value="file is not prepared")
      
      gr.Markdown("<br>")
      with gr.Blocks():
        with gr.Row():
          pre_trained_generator = gr.Textbox(label="Pretrained Generator",
                                            value="/content/gdrive/MyDrive/rvc/pretrain/f0G32k.pth",
                                            placeholder=os.path.join(
                                MODELS_DIR, "pretrained", "v2", "f0D40k.pth"
                            ))
          pre_trained_discriminator = gr.Textbox(label="Pretrained Discriminator",
                                                value="/content/gdrive/MyDrive/rvc/pretrain/f0D32k.pth",
                                                placeholder=os.path.join(
                                MODELS_DIR, "pretrained", "v2", "f0D40k.pth"
                            ))
      
      gr.Markdown("<br>")
      with gr.Blocks():
        with gr.Row():
          run_train_index = gr.Radio(
            choices=["Yes", "No"],
            value="Yes",
            label="Train Index"
          )
          
          reduce_index_size = gr.Radio(
            choices=["Yes", "No"],
            value="No",
            label="Reduce Index Size"
          )
          
          maximum_index_size = gr.Number(
            value=10000, label="Max Index Size"
          )
          
      gr.Markdown("<br>")
      status = gr.Textbox(value="", label="Status")
      
      train_all_button = gr.Button("Training", variant="primary")
      
      train_all_button.click(
        ltrain,
        inputs=[
          model_name,
          version,
          target_sr,
          f0,
          dataset_glob,
          recursive,
          multiple_speakers,
          speaker_id,
          gpu_id,
          num_cpu_process,
          norm_audio_when_preprocess,
          pitch_extraction_algo,
          batch_size,
          augment,
          augment_from_pretrain,
          augment_path,
          speaker_info_path,
          cache_batch,
          num_epochs,
          save_every_epoch,
          save_wav_with_checkpoint,
          fp16,
          pre_trained_generator,
          pre_trained_discriminator,
          run_train_index,
          reduce_index_size,
          maximum_index_size,
          embedding_name,
          embedding_channels,
          embedding_output_layer,
          ignore_cache,
          lr,
          lr_decay,
          seed
        ],
        output=[status]
      )