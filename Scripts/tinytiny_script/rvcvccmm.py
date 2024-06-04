def gen_class(i):
  base = """
class {item}s:
  @staticmethod
  def see():
    return config.{v}
  def add(i:list, base:str):
    # 競合なし
    for x in i:
      x = str(x)
      if find(base, x):
        base = base.replace(x, "")
      else:
        base = base + " " + x
    return [], base\n\n"""
  
  v = "-= Classes =-\n"
  for (n, v, k) in i:
    v += base.format(item=n, v=v)
  
  x = v

  v = ""
  v += "\n\n-= Blocks =-\n"
  base = """
with gr.Accordion({desc}, open=False):
  {item}_INFO = gr.Textbox(visible=False, value="{v}")
  {item} = gr.Textbox(label="現在の値", every=10.0, value={item}s.see, interactive={iterable})
  
  with gr.Column():
    gr.Markdown("Keywords: {kw}")
    
    with gr.Row():
      {item}_i = gr.Dropdown(choices=[{kw}], value=[], multiselect=True, label="キーの追加")
      {item}_a = gr.Button("追加")
      {item}_a.click({item}s.add, [{item}_i, {item}], [{item}_i, {item}])
  
  {item}_p = gr.Button("適用", variant="primary")
  {item}_p.click(update, [{item}, {item}_INFO])
  {item}.change(update_session, [{item}, {item}_INFO])\n\n"""

  for (n, v, k) in i:
    desc = k["desc"]
    kw = k["kw"]
    iterable = not "interactive" in k.keys()
    v += base.format(item=n, v=v, desc=desc, kw=kw, iterable=iterable)
  
  return x, v

i = [
  ("tf", "target_fp", {"kw": "'// (フルパス)'", "desc": "ファイル位置"}),
  ("fnr", "file_named_rule", {"kw": "'{num}', '{model_name}', '{based_fn}', '{aud_format}'", "desc": "ファイルの命名規則"}),
  ("gip", "gradio_ip", {"kw": "'0.0.0.0', '127.0.0.1', '?'", "desc": "Gradio IP", "interactive": ""}),
  ("gp", "gradio_port", {"kw": "!gr.Textboxをgr.Numberへ変更! '?'", "desc": "Gradio Port"}),
  ("bfc", "based_file_compare", {"kw": "", "desc": "元ファイルの比較モード"}),
  ("usr", "_ui_share", {"kw": "", "desc": "Share UIのデフォルト値"}),
  ("dai", "disable_additional_inference", {"kw": "", "desc": "追加推論の無効化"})
]



from LGS.misc.jsonconfig import write_text as w
for t in i:
  v= gen_class([t])
  x = f"{v[0]}\n{v[1]}"
  with open("./rvcvccmm.py.out", "a", encoding="utf-8") as f: f.write(x)
  