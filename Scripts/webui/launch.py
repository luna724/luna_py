# バージョンデータ
version_date = {
# Light Changer
"light_changer": "v1.0",

# CurseForge AutoDownload
"curseforge_autodownload": "v1.0.0",

# Dataset Collector
"dataset_collector": "v4.0pre2",

# jpg2png Converter
"jpg2png_converter": "v1.1.1",

# MP3 to wav Converter
"mp32wav_converter": "v1.1.0",

# Music Collector
"music_collector": "v1.0pre5",

# Picture Collector
"picture_collector": "v1.2.3",

# Audio Augmentation
"audio_augmentation": "v1.0.1"
}

import gradio as gr
import script as luna


with gr.Blocks() as main_interface:
  gr.Markdown(f"lunapy WebUI")
  
  # Light Changer
  with gr.Tab("Light Changer"):
    gr.Markdown(f"\
### Light Changer {version_date['light_changer']}\n\
  Change the brightness of the PC. \n\
  (Work with Windows Only.)")
    inputs_light_changer = gr.Slider(0, 100)
    outputs_light_changer= gr.HTML("")
    buttons_light_changer= gr.Button("Change")
  
  # Audio Augmentation
  with gr.Tab("Audio Augmentation"):
    gr.Markdown(f"\
### Audio Augmentation {version_date['audio_augmentation']}\n\
  Audio augmentation to increase the generalizability of the model")
    
    with gr.Row().style(equal_height=True):
      input_path = gr.Textbox(label="Input Directory")
      input_browse_botton = gr.Button("Browse", scale=1, size="sm")
      input_browse_botton.click(luna.browse_folder, outputs=input_path, show_progress="hidden")
    
    with gr.Row().style(equal_height=True):
      output_path = gr.Textbox(label="Output Directory")
      output_browse_botton = gr.Button("Browse ", scale=1, size="sm")
      output_browse_botton.click(luna.browse_folder, outputs=output_path, show_progress="hidden")
    
    output_type = gr.Radio(choices=["mp3", "flac", "wav", "auto"], value="auto", label="Output Format Types")
    
    inputs_audioaug = [input_path, output_path, output_type]
    outputs_audioaug= gr.HTML("")
    buttons_audioaug= gr.Button("Start")

    
  # ボタンが押されたら
  buttons_light_changer.click(fn=luna.launch_LightChanger,
                inputs=inputs_light_changer,
                outputs=outputs_light_changer)

  buttons_audioaug.click(fn=luna.launch_Audio_Augmentation,
                inputs=inputs_audioaug,
                outputs= outputs_audioaug)
  
  # jpg to png Converter
  with gr.Tab("Picture format Converter"):
    gr.Markdown(f"\
### Picture format Converter {version_date['jpg2png_converter']}\n\
  Image format converter (png, jpg, webp, raw)")
    
    jtp_input_mode = gr.Radio(choices=["directory", "file"], label="File input Type", value="directory")
    with gr.Row().style(equal_height=True):
      jtp_target_dir = gr.Textbox(label="Target Directory")
      jtp_td_browse = gr.Button("Browse", size="sm", scale=1)
      jtp_td_browse.click(luna.browse_folder, outputs=jtp_target_dir, show_progress="hidden")
    
    with gr.Row().style(equal_height=True):
      jtp_target_file = gr.Textbox(label="Target File", value="Only Need Using file Input type")
      jtp_tf_browse = gr.Button("Browse", size="sm", scale=1)
      jtp_tf_browse.click(luna.browse_file, outputs=jtp_target_file, show_progress="hidden")
      
    with gr.Row().style(equal_height=True
    ):
      jtp_out_dir = gr.Textbox(label="Output Directory")
      jtp_od_browse = gr.Button("Browse", size="sm", scale=1)
      jtp_od_browse.click(fn=luna.browse_folder, outputs=jtp_out_dir, show_progress="hidden")
    
    with gr.Row():
      jtp_cv_type = gr.Textbox(label="Convert Type", value="auto")
      jtp_cv_to = gr.Radio(choices=["jpg", "jpeg", "webp", "png", "raw"], label="Convert To", value="png")
      jtp_cv_from = gr.Radio(choices=["any", "jpg", "jpeg", "webp", "png", "raw"], label="Convert From", value="any")
    
    jtp_dof = gr.Checkbox(value=True, label="Delete Previous Format")

    jtp_input = [jtp_input_mode, jtp_target_dir, 
                 jtp_target_file, jtp_out_dir,
                 jtp_dof, jtp_cv_type, jtp_cv_to,
                 jtp_cv_from]
    jtp_outputs = gr.HTML("")
    jtp_buttons = gr.Button("Convert")
    jtp_buttons.click(fn=luna.launch_pics_format_converter,
                      inputs=jtp_input,
                      outputs=jtp_outputs)
    

main_interface.launch()