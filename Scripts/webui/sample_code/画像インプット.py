import numpy as np
import gradio as gr

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189], 
        [0.349, 0.686, 0.168], 
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

demo = gr.Interface(sepia, gr.Image(shape=(200, 200)), "image")
demo.launch()

"""
キーワード引数を使用して、
コンポーネントで使用されるデータ型を設定することもできます
たとえば、関数が NumPy 配列ではなく
画像へのファイル パスを取得するようにしたい場合、
入力Imageコンポーネントは次のように記述できます。

gr.Image(type="filepath", shape=...)
"""