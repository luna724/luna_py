# customtrain.py
# modules.tabs.customtrain

import os
import shutil
import gradio as gr
from multiprocessing import cpu_count
from typing import *

# >_< 
from modules.ui import Tab
from modules.shared import ROOT_DIR, MODELS_DIR
from modules import models, utils
from lib.rvc.train import create_dataset_meta, glob_dataset, train_index, train_model
from lib.rvc.preprocessing import extract_f0, extract_feature, split

# luna
from luna.modules.set_config import update
from luna.lib.train.lr_decay_object import available_function
from luna.lib.train.variable_normalizer import normalize_input

class Customtrain(Tab):
  def title(self):
    return "Customtrain"
  
  def sort(self):
    return 7
  
  def ui(self, outlet):
    def training_start(model_name,
          dataset_glob,
          ignore_cache,
          normalize,
          augment,
          augment_from_pretrain,
          augment_type,
          learning_rate,
          lr_decay,
          lr_decay_function,
          embed_channel,
          embedding_out_layer,
          embedder,
          target_sr,
          f0ing,
          fp16,
          batch_size,
          epoch,
          save_per_n_epoch,
          infer_per_n_epoch,
          pitch_extract_algorithm,
          model_ver,
          using_cpu,
          gpu_id,
          save_wav_with_cp,
          recursive,
          pretrained_generator,
          pretrained_discriminator,
          pretrained_generator_for_al,
          speaker_info,
          train_index,
          reduce_index_size,
          max_index_size,
          when_train_end_close_ui,
          when_train_end_terminate_session,
          remove_dataset,
          save_full_training_parameter,
          model_output_path,
          use_spectral_norm,
          eps,
          segment_size,
          c_mel,
          c_kl,
          seed,
          warmup_epoch):
      # 変数の正則化
      SR_DICT, batch_size, epochs, max_index_size, f0, gpu_ids = normalize_input(batch_size, epochs, max_index_size, f0ing, gpu_id)
      training_dir = os.path.join(MODELS_DIR, "training", "models", model_name)
      
      # ignore cache ならツリーフォルダを削除する
      if os.path.exists(training_dir) and ignore_cache:
        shutil.rmtree(training_dir)
      
      # トレーニングフォルダを作成
      os.makedirs(training_dir, exist_ok=True)
      yield f"Training Directory: {training_dir}"
      
      # データセットを処理、もしないならエラー
      datasets = glob_dataset(
        dataset_glob,
        0,
        multiple_speakers=False,
        recursive=recursive,
        training_dir=training_dir
      )
      
      if len(datasets) == 0:
        yield "ERROR occurpted!"
        return "ERROR: No audio files found."
    
      yield "Preprocessing.."
      split.preprocess_audio(
        datasets,
        SR_DICT[target_sr],
        using_cpu,
        training_dir,
        normalize,
        os.path.join(
          MODELS_DIR,
          "training",
          "mute",
          "0_gt_wavs",
          f"mute{target_sr}.wav",
        )
      )
      
      # f0?
      if f0:
        yield "Extracting f0 Feature.."
        extract_f0.run(
          training_dir,
          using_cpu,
          pitch_extract_algorithm
        )
        yield "Extract f0 Done."
      
      # Extracting Feature
      yield "Extracting Features.."
      
      embedder_filepath, _, embedder_load_from = models.get_embedder(
        embedder_name=embedder
      )
      
    uicfg = update()
    
    with gr.Group():
      with gr.Box():
        with gr.Row():
          with gr.Column():
            model_name = gr.Textbox(
              label="Model Name",
              placeholder="test_Modelv2",
              value=uicfg.model_name
            )
            dataset_glob = gr.Textbox(
              label="Dataset Path",
              placeholder="/dataset/*.wav",
              value=uicfg.dataset_path
            )
          with gr.Column():
            ignore_cache = gr.Checkbox(
              label="Ignore Previous Train Cache",
              value=uicfg.ignore_cache
            )
            normalize = gr.Checkbox(
              label="Normalize Dataset Volume",
              value=uicfg.normalize_audio
            )
            augment = gr.Checkbox(
              label="Augmentation Dataset",
              value=uicfg.augment
            )
            augment_from_pretrain = gr.Checkbox(
              label="Augment Dataset From Pretrain",
              value=uicfg.augment_pretrain
            )
            augment_type = gr.Dropdown(
              choices=["ddPn08 (Original UI)", "lunapy (Unstable)", "Noise Only"],
              label="Augment Script",
              value=uicfg.augment_type
            )
        with gr.Accordion("Model Param",open=True):
          with gr.Row():
            learning_rate = gr.Number(
              label="Learning Rate",
              placeholder="0.0001",
              value=uicfg.lr
            )
            lr_decay = gr.Number(
              label="LR Decay Rate",
              placeholder="0.999875",
              value=uicfg.lr_decay
            )
            lr_decay_function = gr.Dropdown(
              label="LR Decay Function",
              choices=available_function,
              value=uicfg.lr_decay_function
            )
          with gr.Row():
            embed_channel = gr.Radio(
              choices=["256", "768"],
              label="Embedding Channels",
              value=uicfg.embed_channel
            )
            embedding_out_layer = gr.Radio(
              choices=["9", "12"],
              label="Embedding Output Layer",
              value=uicfg.embedding_out_layer
            )
            embedder = gr.Radio(
              choices=["contentvec","hubert", "hubert-base-jp"],
              label="Phone Embedder",
              value=uicfg.embedder
            )
          with gr.Row():
            target_sr = gr.Radio(
              choices=["32k","40k","48k"],
              label="Target Sampling rate",
              value=uicfg.target_sr
            )
            f0ing = gr.Checkbox(
              value=uicfg.f0,
              label="F0 Model"
            )
            fp16 = gr.Checkbox(
              value=uicfg.fp16,
              label="FP16 Model"
            )
          with gr.Row():
            batch_size = gr.Number(
              label="Batch Size",
              placeholder=28,
              value=uicfg.batch_size
            )
            epoch = gr.Number(
              label="Epochs",
              placeholder=240,
              value=uicfg.epochs
            )
            save_per_n_epoch = gr.Slider(
              label="Save per n Epoch",
              minimum=0, maximum=100, step=1,
              value=uicfg.save_per_epoch
            )
            infer_per_n_epoch = gr.Slider(
              label="Infering per n Epoch (Experimental)",
              minimum=0, maximum=100, step=1,
              value=uicfg.infer_per_epoch
            )
          with gr.Row():
            pitch_extract_algorithm = gr.Dropdown(
              label="Pitch Extraction Algorithm",
              choices=["dio", "harvest", "mangio-crepe", "crepe"],
              value=uicfg.pitch_extract_algorithm
            )
            model_ver = gr.Radio(
              choices=["v1", "v2"],
              label="Model Version",
              value=uicfg.model_version
            )
        with gr.Row():
          using_cpu = gr.Slider(
            label="Number of CPU for Preprocessing",
            minimum=1,
            maximum=cpu_count(),
            value=uicfg.cpu_count
          )
          gpu_id = gr.Textbox(
            label="GPU ID for Training",
            value=", ".join([f"{x.index}" for x in utils.get_gpus()])
          )
        with gr.Row():
          save_wav_with_cp = gr.Checkbox(
            label="Save WAV With Checkpoint",
            value=uicfg.save_wav_with_cp
          )
          recursive = gr.Checkbox(
            label="Recursive",
            value=uicfg.recursive
          )
        with gr.Row():
          pretrained_generator = gr.Textbox(
            label="Pretrained Generator Path",
            placeholder="/content/gdrive/MyDrive/rvc-webui/models/pretrained/v2/f0G40k.pth",
            value=uicfg.pretrain_g
          )
          pretrained_discriminator = gr.Textbox(
            label="Pretrained Discriminator Path",
            placeholder="/content/gdrive/MyDrive/rvc-webui/models/pretrained/v2/f0D40k.pth",
            value=uicfg.pretrain_d
          )
        with gr.Row():
          pretrained_generator_for_al = gr.Textbox(
            label="Pretrained Generator (for Additional Learning) Path",
            placeholder="/content/gdrive/MyDrive/rvc-webui/models/checkpoints/pj_ichika-singing_v07.pth",
            value=uicfg.pretrain_g_al
          )
          speaker_info = gr.Textbox(
            label="Speaker Info Path (.npy)",
            placeholder="/content/example.npy",
            value=uicfg.speaker_info
          )
        with gr.Row():
          train_index = gr.Checkbox(
            label="Train Index",
            value=uicfg.train_index
          )
          reduce_index_size = gr.Checkbox(
            label="Reduce Index Size (with kmeans)",
            value=uicfg.reduce_index
          )
          max_index_size = gr.Number(
            label="Max Index Size",
            placeholder=10000,
            value=uicfg.max_index
          )
        with gr.Accordion(label="Optional Option (QoL)",open=False):
          with gr.Row():
            with gr.Column():
              when_train_end_close_ui = gr.Checkbox(
                value="Auto Close UI (When Training Ended)",
                value=uicfg.auto_close
              )
              when_train_end_terminate_session = gr.Checkbox(
                label="Auto Terminate Session (When Training Ended) (Colab Only) (Optional)",
                value=uicfg.terminate_session
              )
              remove_dataset = gr.Checkbox(
                label="Delete Dataset (When Training Ended)",
                value=uicfg.remove_dataset
              )
              save_full_training_parameter = gr.Checkbox(
                label="Save Full Training Parameter",
                value=uicfg.full_parameter
              )
            with gr.Column():
              model_output_path = gr.Textbox(
                label="Model Output Path (pth, index, npy)",
                placeholder="/content/example_path/model1",
                value=uicfg.model_output
              )
        with gr.Accordion(label="Advanced Option",open=False):
          with gr.Row():
            use_spectral_norm = gr.Checkbox(
              label="Use Spectral Norm",
              value=False
            )
            eps = gr.Number(
              label="eps",
              value="1e-9"
            )
            segment_size = gr.Number(
              label="Segment Size",
              value=12800
            )
          with gr.Row():
            c_mel = gr.Number(
              label="c_mel",
              value=45
            )
            c_kl = gr.Number(
              label="c_kl",
              value=1.0
            )
          with gr.Row():
            seed = gr.Number(
              label="Seed",
              value=1234
            )
            warmup_epoch = gr.Number(
              label="Warmup Epoch",
              value=0
            )
      status = gr.Textbox(
        label="Status",
        value="Waiting.."
      )
      
      start = gr.Button(
        value="Training"
      )
        
      start.click(
        fn=training_start,
        inputs=[
          model_name,
          dataset_glob,
          ignore_cache,
          normalize,
          augment,
          augment_from_pretrain,
          augment_type,
          learning_rate,
          lr_decay,
          lr_decay_function,
          embed_channel,
          embedding_out_layer,
          embedder,
          target_sr,
          f0ing,
          fp16,
          batch_size,
          epoch,
          save_per_n_epoch,
          infer_per_n_epoch,
          pitch_extract_algorithm,
          model_ver,
          using_cpu,
          gpu_id,
          save_wav_with_cp,
          recursive,
          pretrained_generator,
          pretrained_discriminator,
          pretrained_generator_for_al,
          speaker_info,
          train_index,
          reduce_index_size,
          max_index_size,
          when_train_end_close_ui,
          when_train_end_terminate_session,
          remove_dataset,
          save_full_training_parameter,
          model_output_path,
          use_spectral_norm,
          eps,
          segment_size,
          c_mel,
          c_kl,
          seed,
          warmup_epoch
        ],
        outputs=[status]
      )