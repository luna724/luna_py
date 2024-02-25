import gradio as gr
import os
import subprocess
from tkinter import Tk, filedialog

from ui import Tabs

class multitrack_separate(Tabs):
  def variable(self):
    return "MultiTrack video Seperator"
  def index(self):
    return 1
  
  def ui(self, outlet):
    def show_state_from_checkbox(status: bool):
      return gr.update(visible=status), gr.update(visible=not status)
    def browse_file():
      root = Tk()
      root.attributes("-topmost", True)
      root.withdraw()
      
      filenames = filedialog.askopenfilenames()
      if len(filenames) > 0:
          root.destroy()
          return str(filenames)
      else:
          root.destroy()
          return ""
    def browse_folder():
      root = Tk()
      root.attributes("-topmost", True)
      root.withdraw()

      filename = filedialog.askdirectory()
      if filename:
          if os.path.isdir(filename):
              root.destroy()
              return str(filename)
          else:
              root.destroy()
              return str(filename)
      else:
          root.destroy()
          return ""
      
    def launch(
      target_file, sepmode, sepout, vid_codec="copy", audio_codec="wav16",
      out_dir="/", use_cui=False 
    ):
      filename = os.path.basename(target_file)
      name = os.path.splitext(filename)[0]
      outvid = os.path.join(out_dir) + "/"+name
      out = os.path.join(out_dir, "audios")+"/"+name
      
      if audio_codec=="wav16":
        acdc = "pcm_s16le"
      
      cmd = f'ffmpeg -i "{target_file}" -map 0:0? -vcodec copy "{outvid}.mp4" -map 0:1? -vn -acodec {acdc} "{out}_audio-track01.wav"'
      
      if sepout < 2:
        return "Failed. Track counts are need 2+"
        
      for x in range(2, sepout+1):
        # 1引いた回数実行
        new = ' -map 0:{x}? -vn -acodec {acdc} "{out}_audio-track0{x}.wav"'
        cmd += new 
      
      def mkdir(*args):
        path = os.getcwd()
        for x in args:
          path = os.path.join(path, x)
        os.makedirs(path, exist_ok=True)
        return
      
      os.makedirs(out_dir, exist_ok=True)
      os.makedirs(os.path.join(out_dir, "audios"), exists_ok=True)
      
      if sepmode == "FFmpeg-CUI":
        yield f"parsing with {sepmode}.."
        subprocess.run(
          cmd
        )
      
      yield "Done."
    
    with gr.Blocks():
      
      with gr.Row():
        target_file = gr.Textbox(label="Target file(s)",lines=2)
        isdir = gr.Checkbox(label="directory input mode", value=False)
        locate = gr.Button("Browse", visible=True)
        locate_dir = gr.Button("Browse dir", visible=False)
        locate.click(browse_file, outputs=[target_file])
        locate_dir.click(browse_folder, outputs=[target_file])
        isdir.change(show_state_from_checkbox, isdir, outputs=[locate_dir, locate])
      
      with gr.Group():
        with gr.Column():
          sepmode = gr.Dropdown(choices=["FFmpeg-CUI", "FFmpeg-python"], label="Sep mode", value="FFmpeg-CUI")
          
          with gr.Row():
            vid_codec = gr.Dropdown(choices=["copy"], value="copy", label="video codec")
            vid_format = gr.Dropdown(choices=["mp4"], value="mp4", label="output Video format")
          with gr.Row():
            audio_codec = gr.Dropdown(choices=["copy", "wav16"], label="Audio Codec", value="wav16")
            audio_format = gr.Dropdown(choices=["wav"], value="wav", label="Audio format")
          
        track_count = gr.Slider(2, 6, value=3, label="audio Track count", step=1)
      
      with gr.Row():
        out_path = gr.Textbox(label="Output path", value="/")
        opb = gr.Button("Browse")
        opb.click(browse_folder, outputs=out_path)
      
      status = gr.Textbox(label="Status")
      run = gr.Button("Run")
      run.click(launch, inputs=[
        target_file, sepmode, track_count, vid_codec, audio_codec, out_path
      ], outputs=status)