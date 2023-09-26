import gradio as gr
from jsoncfg_legacy import jsonconfig

# インスタンス化
jsoncfg = jsonconfig() 

# 変数を読み込みまくる
with open("./model_db_view/data/info_view.txt", "r") as f:
  info_view = f.read()

model_data = jsoncfg.read("./model_db_view/data/model_data.json")
model_list = model_data.keys()

def load(model_name):
  data = jsoncfg.read("./model_db_view/data/model_data.json")

  # 読み込み
  target = data[model_name]
  
  # 摘出
  """Example
  {"version":"v2",
  "train":{"log_interval":200,"seed":1234,"epochs":20000,"learning_rate":0.0001,"betas":[0.8,0.99],"eps":1e-9,"batch_size":4,
  "fp16_run":true,"lr_decay":0.999875,"segment_size":11520,"init_lr_ratio":1,"warmup_epochs":0,"c_mel":45,"c_kl":1.0},
  "data":{"max_wav_value":32768.0,"sampling_rate":48000,"filter_length":2048,"hop_length":480,"win_length":2048,"n_mel_channels":128,"mel_fmin":0.0,"mel_fmax":null},
  "model":{"inter_channels":192,"hidden_channels":192,"filter_channels":768,"n_heads":2,"n_layers":6,"kernel_size":3,"p_dropout":0,"resblock":"1","resblock_kernel_sizes":[3,7,11],"resblock_dilation_sizes":[[1,3,5],[1,3,5],[1,3,5]],"upsample_rates":[10,6,2,2,2],"upsample_initial_channel":512,"upsample_kernel_sizes":[16,16,4,4,4],
  "use_spectral_norm":false,"gin_channels":256,"emb_channels":768,
  "spk_embed_dim":109}}
  """
  model_ver = target["version"]
  lr = target["train"]["learning_rate"]
  lr_decay = target["train"]["lr_decay"]
  fp16 = target["train"]["fp16_run"]
  spectral_norm = target["model"]["use_spectral_norm"]
  emb_ch = target["model"]["emb_channels"]
  
# UI定義
with gr.Blocks() as iface:
  gr.Markdown(info_view)
  with gr.Row():
    target_model_name = gr.Dropdown(choices=model_list, value="phase1_ichika2-1.pth", label="Target Model")
  

# 実行
iface.launch()