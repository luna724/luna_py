import gradio as gr
import LGS.misc.jsonconfig as jsoncfg
import os

from modules.shared import ROOT_DIR, language, database

def build_ui():
  l = language("/ui/database.py", "raw")
  
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
  
  with gr.Blocks() as i:
    with gr.Column():
      negatives = gr.Textbox(label=l["negative"], value=database("negative"))
      ad_positives = gr.Textbox(label=l["ad_positive"], value=database("ad_pos"))
      ad_negatives = gr.Textbox(label=l["ad_negative"], value=database("ad_neg"))
    with gr.Accordion(l["accordion1"], open=False):
      negative = gr.Textbox(label=l["negative"], value=database("negative"))
      ad_positive = gr.Textbox(label=l["ad_positive"], value=database("ad_pos"))
      ad_negative = gr.Textbox(label=l["ad_negative"], value=database("ad_neg"))
      
      btn = gr.Button(l["acc1_btn"])
      btn.click(
        fn=modify_database,inputs=[negative, ad_positive, ad_negative],
        outputs=[negatives, ad_positives, ad_negatives]
      )
  
  return ("タブだよ", lambda: i)
