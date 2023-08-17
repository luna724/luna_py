import gradio as gr
import os
from tkinter import Tk, filedialog


def on_browse(data_type):
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    if data_type == "Files":
        filenames = filedialog.askopenfilenames()
        if len(filenames) > 0:
            root.destroy()
            return str(filenames)
        else:
            filename = "Files not seleceted"
            root.destroy()
            return str(filename)

    elif data_type == "Folder":
        filename = filedialog.askdirectory()
        if filename:
            if os.path.isdir(filename):
                root.destroy()
                return str(filename)
            else:
                root.destroy()
                return str(filename)
        else:
            filename = "Folder not seleceted"
            root.destroy()
            return str(filename)


def main():
    with gr.Blocks() as demo:
        data_type = gr.Radio(choices=["Files", "Folder"], value="Files", label="Offline data type")
        input_path = gr.Textbox(label="Select Multiple videos", scale=5, interactive=False)
        image_browse_btn = gr.Button("Browse", min_width=1)
        image_browse_btn.click(on_browse, inputs=data_type, outputs=input_path, show_progress="hidden")
    return demo


demo = main()
demo.launch(inbrowser=True)

    # ボタンがクリックされた時のアクションを指定
    # テキスト反転
    text_button.click(flip_text, inputs=text_input, outputs=text_output)
    # 画像反転
    image_button.click(flip_image, inputs=image_input, outputs=image_output)
