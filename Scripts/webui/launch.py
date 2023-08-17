# バージョンデータ
version_date = {
# Light Changer
"light_changer": "v1.0",

# CurseForge AutoDownload
"curseforge_autodownload": "v1.0.0",

# Dataset Collector
"dataset_collector": "v4.0pre2",

# jpg2png Converter
"jpg2png_converter": "v1.1.0",

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
    input_path = gr.Textbox(label="Input Directory")
    input_browse_botton = gr.Button("Browse", scale=1, size="sm")
    input_browse_botton.click(luna.browse_folder, outputs=input_path, show_progress="hidden")
    
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
  
main_interface.launch()