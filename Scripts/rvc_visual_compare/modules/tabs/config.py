import gradio as gr

from modules.config_manager import update_config, update_session_config, reload_config, config, sys_config
from modules.ui import UiTabs
from modules.config_ui import *

class Config(UiTabs):
  def title(self):
    return "Config manager"
  
  def index(self):
    return 1
  
  def ui(self, outlet):
    def update(v, id:str):
      update_config(id, v)
      gr.Info("適用に成功しました。")
    def update_session(v, id:str):
      update_session_config(id, v)
    
    cgui = hasattr(sys_config, "config_gui_mode")
    
    with gr.Blocks():
      gr.Markdown("config manager - β1.1-r1 - gradio support")
      
      with gr.Accordion("Jupyter mode (ipynb mode)", open=True):
        with gr.Accordion("生成ブックのパスの命名規則", open=False):
          idr_INFO = gr.Textbox(visible=False, value="ipynb_dir_rule")
          idr = gr.Textbox(label="現在の値", every=10.0, value=idrs.see)
          
          with gr.Column():
            gr.Markdown("Keywords: {datetime}")
            
            with gr.Row():
              idr_i = gr.Dropdown(choices=["{datetime}"], value=[], multiselect=True, label="キーの追加")
              idr_a = gr.Button("追加")
              idr_a.click(idrs.add, [idr_i, idr], [idr_i, idr])
          
          idr_p = gr.Button("適用", variant="primary")
          idr_p.click(update, [idr, idr_INFO])
          idr.change(update_session, [idr, idr_INFO])
      
        with gr.Accordion("生成ブックの命名規則", open=False):
          inr_INFO = gr.Textbox(visible=False, value="ipynb_name_rule")
          inr = gr.Textbox(label="現在の値", every=10.0, value=inrs.see)
          
          with gr.Column():
            gr.Markdown("Keywords: !")
            
            with gr.Row():
              inr_i = gr.Dropdown(choices=["{datetime}", "{model_name}", "{sha}"], value=[], multiselect=True, label="キーの追加")
              inr_a = gr.Button("追加")
              inr_a.click(inrs.add, [inr_i, inr], [inr_i, inr])
          
          inr_p = gr.Button("適用", variant="primary")
          inr_p.click(update, [inr, inr_INFO])
          inr.change(update_session, [inr, inr_INFO])

      with gr.Accordion("グローバル設定", open=True):
        with gr.Accordion("ファイル位置", open=False):
          tf_INFO = gr.Textbox(visible=False, value="target_fp")
          tf = gr.Textbox(label="現在の値", every=10.0, value=tfs.see, interactive=True)
          
          with gr.Column():
            gr.Markdown("Keywords: '// (フルパス)'")
            
            with gr.Row():
              tf_i = gr.Dropdown(choices=['// (フルパス)'], value="", multiselect=False, label="キーの追加")
              #tf_a = gr.Button("追加")
              tf_i.change(tfs.add, [tf_i, tf], [tf_i, tf])
          
          tf_p = gr.Button("適用", variant="primary")
          tf_p.click(update, [tf, tf_INFO])
          tf.change(update_session, [tf, tf_INFO])
        
        with gr.Accordion("ファイルの命名規則", open=False):
          fnr_INFO = gr.Textbox(visible=False, value="file_named_rule")
          fnr = gr.Textbox(label="現在の値", every=10.0, value=fnrs.see, interactive=True)
          
          with gr.Column():
            gr.Markdown("Keywords: '{num}', '{model_name}', '{based_fn}', '{aud_format}'")
            
            with gr.Row():
              fnr_i = gr.Dropdown(choices=['{num}', '{model_name}', '{based_fn}', '{aud_format}'], value=[], multiselect=True, label="キーの追加")
              fnr_i.change(fnrs.add, [fnr_i, fnr], [fnr_i, fnr])
          
          fnr_p = gr.Button("適用", variant="primary")
          fnr_p.click(update, [fnr, fnr_INFO])
          fnr.change(update_session, [fnr, fnr_INFO])
        
        with gr.Accordion("追加推論の無効化", open=False):
          dai_INFO = gr.Textbox(visible=False, value="disable_additional_inference")
          dai = gr.Checkbox(label="現在の値", every=10.0, value=dais.see, interactive=True)
          dai_p = gr.Button("適用", variant="primary")
          dai_p.click(update, [dai, dai_INFO])
          dai.change(update_session, [dai, dai_INFO])
        
        with gr.Accordion("元ファイルの比較モード", open=False):
          bfc_INFO = gr.Textbox(visible=False, value="based_file_compare")
          bfc = gr.Checkbox(label="現在の値", every=10.0, value=bfcs.see, interactive=True)
          bfc_p = gr.Button("適用", variant="primary")
          bfc_p.click(update, [bfc, bfc_INFO])
          bfc.change(update_session, [bfc, bfc_INFO])
        
      with gr.Accordion("Gradio mode", open=True):
        with gr.Accordion("Gradio IP", open=False):
          gip_INFO = gr.Textbox(visible=False, value="gradio_ip")
          gip = gr.Textbox(label="現在の値", every=1.0, value=gips.see, interactive=False)
          
          with gr.Column():
            gr.Markdown("Keywords: '0.0.0.0', '127.0.0.1', '?'")
            
            with gr.Row():
              gip_i = gr.Dropdown(choices=['0.0.0.0', '127.0.0.1', '?'], value="", multiselect=False, label="キーの追加")
              #gip_a = gr.Button("追加")
              gip_i.change(gips.add, [gip_i, gip], [gip_i, gip])
          
          gip_p = gr.Button("適用", variant="primary")
          gip_p.click(update, [gip, gip_INFO])
          gip.change(update_session, [gip, gip_INFO])
        
        with gr.Accordion("Gradio Port", open=False):
          gp_INFO = gr.Textbox(visible=False, value="gradio_port")
          gp = gr.Number(label="現在の値", every=10.0, value=gps.see, interactive=True)
          
          with gr.Column():
            gr.Markdown("Keywords: '?'")
            
            with gr.Row():
              gp_i = gr.Dropdown(choices=['?'], value="", multiselect=False, label="キーの追加")
              gp_i.change(gps.add, [gp_i, gp], [gp_i, gp])
          
          gp_p = gr.Button("適用", variant="primary")
          gp_p.click(gps.update, [gp, gp_INFO])
          gp.change(update_session, [gp, gp_INFO])
        
        with gr.Accordion("Share UIのデフォルト値", open=False):
          usr_INFO = gr.Textbox(visible=False, value="_ui_share")
          usr = gr.Checkbox(label="現在の値", every=10.0, value=usrs.see, interactive=True)
          usr_p = gr.Button("適用", variant="primary")
          usr_p.click(update, [usr, usr_INFO])
          usr.change(update_session, [usr, usr_INFO])