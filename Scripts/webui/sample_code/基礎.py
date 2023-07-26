import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    
demo.launch()


""" 

Hello World!
テキストインプットを受け取り、Hello {name}! を返す

"""