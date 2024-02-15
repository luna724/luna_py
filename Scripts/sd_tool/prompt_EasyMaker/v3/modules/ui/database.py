import gradio as gr
import LGS.misc.jsonconfig as jsoncfg
import os

from modules.shared import ROOT_DIR, language, database
from webui import UiTabs

class Database(UiTabs):
  l = language("/ui/database.py", "raw")
  
  def variable(self):
    return [Database.l["tab_title"]]
  
  def index(self):
    return 1
  
  def ui(self, outlet):
    def modify_database(neg, adp, adn):
      new = {
        "negative": neg,
        "ad_pos": adp,
        "ad_neg": adn
      }
      
      jsoncfg.write(
        new, os.path.join(ROOT_DIR, "database", "v3", "database_ui.json")
      )
      
      d = database(None)
      return d["negative"], d["ad_pos"], d["ad_neg"]
  
    with gr.Blocks():
      with gr.Column():
        negatives = gr.Textbox(label=Database.l["negative"], value=database("negative"))
        ad_positives = gr.Textbox(label=Database.l["ad_positive"], value=database("ad_pos"))
        ad_negatives = gr.Textbox(label=Database.l["ad_negative"], value=database("ad_neg"))
      with gr.Accordion(Database.l["accordion1"], open=False):
        negative = gr.Textbox(label=Database.l["negative"], value=database("negative"))
        ad_positive = gr.Textbox(label=Database.l["ad_positive"], value=database("ad_pos"))
        ad_negative = gr.Textbox(label=Database.l["ad_negative"], value=database("ad_neg"))
        
        btn = gr.Button(Database.l["acc1_btn"])
        btn.click(
          fn=modify_database,inputs=[negative, ad_positive, ad_negative],
          outputs=[negatives, ad_positives, ad_negatives]
        )
