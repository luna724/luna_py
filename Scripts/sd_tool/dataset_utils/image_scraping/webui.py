from image_scraping.func import *

def create_ui(*args):
  component = gr.Blocks()
  
  with component:
    gr.Markdown("Image scraping")
    
    mode = gr.Dropdown(
      choices=["Googleレンズ検索", "Googleテキスト検索", "resize Directory"],
      value="Googleテキスト検索",
      interactive=True, mode="モード選択", type="index")
    
    with gr.Column():
      text_engine = gr.Textbox(label="テキスト語句", max_lines=2, visible=False)
      image_engine = gr.Image(label="検索対象画像", type="pil", visible=False)
      with gr.Group(visible=False) as resize_engine:
        with gr.Row():
          resize_dir = gr.Textbox(label="処理対象パス", interactive=False)
          rd_browse = gr.Button("参照")
          rd_browse.click(
            browse_file, outputs=resize_dir
          )
    mode.change(
      whenModeChanged, mode, [text_engine, image_engine, resize_engine]
    )
    
    with gr.Row():
      with gr.Row():
        output_dir = gr.Textbox(label="出力先ディレクトリ", scale=7, value="./image_scraping/out")
        od_browse = gr.Button("参照", scale=2)
        od_browse.click(
          browse_file, outputs=output_dir
        )
      out_fn = gr.Textbox(label="画像ファイル名", max_lines=1, scale=2)
      exts = gr.Dropdown(
        ["png", "jpg", "keep"], value="png", label="出力ファイル拡張子",
        scale=1
      )
    
    with gr.Row():
      cd = gr.Slider(0, 2, value=0, step=0.01, label="クールダウン (0の場合自動調整)", scale=3)
      sm = gr.Checkbox(label="セーフモード", scale=1, value=False)
    
    with gr.Accordion("出力"):
      image = gr.Image(label="取得した画像", show_download_button=False, interactive=False)
      log = gr.Textbox(label="出力ログ", interactive=False, max_lines=75)
      
    main = gr.Button("取得")
    main.click(
      fn=run,
      inputs=[
        mode, text_engine, image_engine, resize_dir,
        output_dir, out_fn, exts,
        cd, sm
      ],
      outputs=[
        image, log
      ]
    )
    
  return component

def ui(*args):
  create_ui().queue(
    64
  ).launch(
    inbrowser=True
  )
  return "Terminated."