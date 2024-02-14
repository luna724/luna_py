import gradio as gr

def build_ui():
  i = gr.Blocks()
  
  with i:
    textbox = gr.Textbox(label="HELLO this is called by test.py")
    
    
  
  
  return ("testTAB", lambda:i)