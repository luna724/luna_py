from pydantic import BaseModel
from LGS.misc.jsonconfig import read as read_json, write as write_json
import os

class sysCfg(BaseModel):
  """注; ここの変数にあるコメントは更新されません。"""
  ipynb_basic: str
  """生成されるノートブックのテンプレート"""
  md_template: str
  """生成されるmdのテンプレート"""
  crt_method: str # "%Y%m%d%H%M%S"
  """datetime.datetime.now().strftime() にて使われる値"""
  known_model_names: list
  use_known_model_names_to_parse_fn: bool
  auto_open_browser: bool

class cfgMain(BaseModel):
  """注: ここの変数にあるコメントは更新されません。"""
  
  @staticmethod
  def convert_path(v):
    if v.startswith("//"):
      v = v.strip("//")
    else:
      v = os.path.join(os.getcwd(), v)
    
    return v
  
  target_fp: str 
  """使用法1 にある指定位置。rvc_visual_compare からの相対パスだが、//から開始するとフルパスと認識する"""
  file_named_rule: str
  """ 使用法1 にある命名規則。{model_name}, {based_fn} がないとエラーを返す。{num}, {any}, {aud_format} は任意追加。{any}の仕様は誤作動を防ぐため、前後をそこにしかない文字で囲うことを推奨。{aud_format}は mp3, wav, flac にのみ適用される"""
  ipynb_dir_rule: str
  ipynb_name_rule: str
  """使用法(ipynb mode)3にあるファイル名。変数は {datetime}, {model_name}, {sha} を受け付ける。すべては任意で {datetime}は現在時刻、{model_name}はモデルの絞り込みで指定されたモデル名、{sha}はランダム文字列の sha256。これらは {datetime} -> {model_name} -> {sha} の順に解析され、前のものでエラーが発生した場合、後ろの機能は動作しない"""
  gradio_ip: str
  """Gradio UIに使用するIP。?を指定すると Gradio に None を渡す"""
  gradio_port: int
  """	Gradio UIに使用するポート。?を指定するとGradio に Noneを渡す"""
  lunapy_compatibility: bool
  """オーディオと同じ名前の .info ファイルをそのオーディオの生成情報として評価モードの合計値の平均値、中央値の算出に使用する。現在は何の意味もない"""
  based_file_compare: bool
  """モデルではなく、変換に使用した元ファイルによる違いの比較を行う"""
  _ui_share: bool
  """Gradio UIの share 引数の値。--share と引数に追加することでも設定可能"""
  disable_additional_inference: bool
  """	追加推論機能の無効化。無効化を行うと、PyTorch等のインポートも停止され、使用RAM量が大幅に軽減されたり、CUDA未インストール環境でも実行可能になる。"""
  
  
  sys: dict
  def update_sys(self):
    return sysCfg(**self.sys)
config = cfgMain(**read_json(os.path.join(os.getcwd(), "config.json")))
sys_config = config.update_sys()


def update_config():
  global config
  global sys_config
  
  config = cfgMain(**read_json(os.path.join(os.getcwd(), "config.json")))
  sys_config = config.update_sys()

def reload_config():
  update_config()


def update_session_config(name:str, value):
  """今セッションでのみ変更が適用されるコンフィグ
  update_config() を実行すると元に戻る"""
  global config
  
  setattr(config, name, value)


def update_config(name:str, value):
  fn = os.path.join(os.getcwd(), "config.json")
  data:dict = read_json(fn)
  
  if name in data.keys():
    data[name] = value
  
  else:
    if name in data["sys"].keys():
      data["sys"][name] = value
    
    else:
      print(f"stderr: [update_config]: [{name}]: unknown config.")
      return
  
  write_json(data, fn)
  