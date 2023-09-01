# バージョンデータ
version_date = {
# Light Changer
"light_changer": "v1.0",

# CurseForge AutoDownload
"curseforge_autodownload": "v2.2",

# Dataset Collector
"dataset_collector": "v4.0pre3",

# jpg2png Converter
"jpg2png_converter": "v1.1.1",

# MP3 to wav Converter
"mp32wav_converter": "v1.1.0",

# Music Collector
"music_collector": "v1.0pre5",

# Picture Collector
"picture_collector": "v1.2.4",

# Audio Augmentation
"audio_augmentation": "v1.0.2",

# Lunpy WebUI
"lunapy_gradioui": "v1.0pre5",

# Audio Duration Calculator
"audio_duration_calculator": "v1.0pre3",

# Audio Properties Auto Setting
"audio_properties_auto_setting": "v1.1"
}

import gradio as gr
import script as luna


with gr.Blocks() as main_interface:
  gr.HTML(f"lunapy WebUI <strong>{version_date['lunapy_gradioui']}</strong>")
  
  # Light Changer
  with gr.Tab("Light Changer"):
    gr.Markdown(f"\
### Light Changer {version_date['light_changer']}\n\
  Change the brightness of the PC. \n\
  (Work with Windows Only.)")
    inputs_light_changer = gr.Slider(0, 100, label="Light Level", value=50)
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
    
    with gr.Row().style(equal_height=True):
      output_type = gr.Radio(choices=["mp3", "flac", "wav", "auto"], value="auto", label="Output Format Types")
      augment_percantage = gr.Slider(0, 100, value=100, label="Augment Activate %")
      
    inputs_audioaug = [input_path, output_path, output_type, augment_percantage]
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
    
  with gr.Tab("Audio Duration Calculator"):
    gr.Markdown(f"### Audio Duration Calculator {version_date['audio_duration_calculator']}\n\tTarget Directory Audio File Duration Calculation")
    
    with gr.Blocks():
      adc_outptus = gr.Markdown("| Total Duration | Total Duration (seconds) | Total Duration (millseconds) |\n| --- | --- | --- |\n| 0h 0m 0s | 0s | 0ms |")
      gr.HTML("<br>")
      adc_btn = gr.Button("Calculate")
      gr.HTML("<br><br>")
    
    with gr.Row().style(equal_height=True):
      adc_target_dir = gr.Textbox(label="Target Directory")
      adc_td_browse = gr.Button("Browse", size="sm", scale=1)
      adc_td_browse.click(luna.browse_folder, outputs=adc_target_dir, show_progress="hidden")
    
    adc_td_min_silent = gr.Slider(0, 100000, label="Minimum length of silent time to be excluded from the calculation (ms)", value=1000)
    
    with gr.Accordion("Advanced Option", open=False):
      with gr.Row():
        adc_splitsec = gr.Textbox(label="Split After (Syntax: 0h 0m 0s 0ms)", value="Example: 0h 0m 45s 0ms")
        adc_split_output = gr.Textbox(label="Split Output Directory")
        adc_split_output_browse = gr.Button("Browse", size="sm", scale=1)
        adc_split_output_browse.click(luna.browse_folder, outputs=adc_split_output, show_progress="hidden")
        adc_split_skip = gr.Slider(0, 1000, label="Random Split Choice Skip Chance (1 = 0.1%)", value=500)
    
    adc_input = [adc_target_dir, adc_td_min_silent, adc_splitsec, adc_split_output, adc_split_skip]
    adc_btn.click(fn=luna.launch_audio_duration_calculator,
                  inputs=adc_input,
                  outputs=adc_outptus)
  
  with gr.Tab("Audio Properties Auto Setting"):
    gr.Markdown(f"### Audio Properties Auto Setting {version_date['audio_properties_auto_setting']}\n\Audio File Properties Auto-Setup (from Template)")

    with gr.Row():
      apas_target_dir = gr.Textbox(label="Target Directory")
      apas_td_brw = gr.Button("Browse")
      apas_td_brw.click(luna.browse_folder, outputs=apas_target_dir, show_progress="hidden")
    
    gr.Markdown(f"\nTemplate Set  (if not use template, not write anything)")
    with gr.Row():
      apas_t_title = gr.Textbox(label="Title")
      apas_t_artist = gr.Textbox(label="Artist")
    with gr.Row():
      apas_t_album = gr.Textbox(label="Album")
      apas_t_genre = gr.Textbox(label="Genre")
    with gr.Row():
      apas_t_composer = gr.Textbox(label="Composer")
      
    apas_songname = gr.Checkbox(label="assignment song name to title", value=False)
    apas_composer_autogen = gr.Checkbox(label="Composer Auto Collect (from Google)", value=False)
    
    with gr.Row():
      gr.Markdown("Only need if using \"Composer Auto Collect\" or \"Song name To Title\"  \n ### Only one of them is required")
      apas_songname_pattern = gr.Textbox(label="Song Name Pattern (re.extract) ", value="Example: (.*?)\\ Gamesize")
      apas_songname_pattern2 = gr.Textbox(label="Song Name Pattern (.replace().strip())", value="Example: Gamesize")
    
    apas_inputs = [apas_target_dir, apas_composer_autogen,
                   apas_songname_pattern, apas_songname_pattern2,
                   apas_t_title, apas_t_artist,
                   apas_t_album, apas_t_genre,
                   apas_t_composer, apas_songname]
    
    apas_outputs = gr.HTML("")
    
    apas_btn = gr.Button("Start")
    apas_btn.click(fn=luna.Audio_Properties_Auto_Setting,
                   inputs=apas_inputs,
                   outputs=apas_outputs)
    

        
main_interface.launch(inbrowser=True)