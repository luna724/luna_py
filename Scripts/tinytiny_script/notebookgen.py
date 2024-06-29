import os
import json
from typing import *

class Database:
  def __init__(self):
    self.mode_detector = {
      "vae": ("install_vae('{fn}')", ".vae"),
      "cp": ("install_ckpt('{fn}')", ".safetensors"),
      "lora": ("install_lora('{fn}')", ".safetensors"),
      "cnet": ("install_cnmodel('{fn}')", ".pt"),
      "lycoris": ("install_lora('{fn}')", ".safetensors")
    }
    self.drive_path_detector = {
      "cp": ("", "/content/gdrive/MyDrive/SD_Model/{fn}"),
      "lora": ("LoRA", "/content/gdrive/MyDrive/SD_Model/LoRA/{fn}"),
      "cnet": ("ControlNet", "/content/gdrive/MyDrive/SD_Model/ControlNet/{fn}"),
      "lycoris": ("LoRA", "/content/gdrive/MyDrive/SD_Model/LoRA/{fn}"),
      "vae": ("VAE", "/content/gdrive/MyDrive/SD_Model/VAE/{fn}")
    }
    
  @staticmethod
  def lycon(model:str) -> str:
    if model == "lycon": return "lycoris"
    else: return model
  
  def get_drive_path(self, model:str) -> str:
    return self.drive_path_detector[self.lycon(model)]
  
  def convert_dn(self, dn:str, model:str) -> Tuple[str, str]:
    ins = "Download_" + os.path.basename(dn).title().replace(" ", "_")
    fn = dn.lower().replace(" ", "")
    model = self.lycon(model)

    if os.path.splitext(fn)[1] == "":
      fn += self.mode_detector[model][1]
    
    return (ins, fn)
  
  def get_install_from_model(self, model:str, dn:str) -> str:
    """model, dn を受け取り、モデル注入コードを返す"""
    # dn の変換
    ins, fn = self.convert_dn(dn, model)
    
    model = self.lycon(model)
    ln2, _ = self.mode_detector[model]
    ln2 = ln2.format(fn=fn)
    return "{ins} = False #@param {{type: \"boolean\"}}\nif {ins}: {ln2}\n".format(ins=ins, ln2=ln2)

    
class Main:
  def __init__(self, allow_custom_type:bool=False):
    self.allow_custom_type = allow_custom_type
    self.database = Database()
    self.displays: List[str] = []
    self.available_type: List[str] = [
      "aom", "anything", "cuteyukimix", "fuwafuwa", "other-sdcp", "prsk", "bluearchive", "prcn", "touhou", "genshin",
      "honkai", "other_ch", "bondage_only", "bondage_suspension", "cloth_full", "cloth_breasts", "cloth_legs", "ears",
      "masturbation", "whb", "tentacles", "pose_for_nude", "in_any", "other_pose", "yuri", "styling", "color", "quality",
      "other", None, "ti", "cn_model", "sex"
    ]
    self.models:List[str] = ["vae", "cp", "lora", "lycoris", "lycon", "cnet"]
    self.links:List[str] = []
    
    self.values:List[Tuple[str, str, str, str|None]] = []
  
  def join(self, item:Tuple[dict] =
          ({"dn": "DISPLAY_NAME", "type": "Literal[..]", "model": "Literal[vae, cp, lora, lycoris]", "link": "Optional. Install URL for wget function"})) -> None:
    for x in item:
      dn = x["dn"]
      typo = x["type"]
      model = x["model"]
      url = None
      
      try:
        url = x["link"]
      except KeyError:
        pass
      
      if dn in self.displays:
        continue
      if not typo in self.available_type and not self.allow_custom_type:
        print(f"[WARN]: {dn}] typeが不明です。 ({typo})")
        continue
      if not model in self.models:
        print(f"[WARN]: {dn}: modelが不明です。 ({model})")
        continue
      if url is not None and url in self.links:
        print(f"[WARN]: {dn}: linkが定義済みです、重複したモデルがないか確認してください。 ({url})")
        continue
      
      # Preparation
      self.displays.append(dn)
      if url is not None:
        self.links.append(url)
      
      tpl = (
        dn, typo, model, url
      )
      self.values.append(tpl)
    
    print("[join]: done.")
  
  def build_command(self, i:tuple, mode:Literal["normal", "wget"] = "normal") -> str:
    cmd = ""
    if mode == "normal":
      dn = i[0]
      model = i[2]
      
      cmd += self.database.get_install_from_model(model, dn)
    
    elif mode == "wget":
      dn = i[0]
      model = i[2]
      url = i[3]
      
      if url is None:
        pass
      
      else:
        _, fn = self.database.convert_dn(dn, model)
        drive_path = self.database.get_drive_path(model)
        cmd += f'!wget "{url}" -O "/content/gdrive/MyDrive/SD_Model/{drive_path[0]}/{fn}"\n'
    
    return cmd
  
  def start(self):
    self.cmds = {"??wget": ""}
    for x in self.values:
      # type に分類しコマンドを作成
      typo = x[1]
      dn = x[0]
      model = x[2]
      url = x[3]
      
      if not typo in self.cmds.keys():
        self.cmds[typo] = ""
      
      self.cmds[typo] += self.build_command(x)
      
      self.cmds["??wget"] += self.build_command(x, "wget")
    
    self.notebook_string = ""
    
    for k, v in self.cmds.items():
      self.notebook_string += f"-=-=-= {k} =-=-=-\n{v}\n\n"
    
    # セーブwith
    with open("./notebookgen.py.out", "w", encoding="utf-8") as f:
      f.write(self.notebook_string)

    print("Done.")

i = (
  # {"dn": "Shiny_Wet_Skin", "type": "cloth_full", "model": "lycoris", "link": "https://civitai.com/api/download/models/57459"},
  # {"dn": "Yamioti_Corruption", "type": "cloth_full", "model": "lora", "link": "https://civitai.com/api/download/models/415699"},
  # {"dn": "All_fours_Yotunbai", "type": "other_pose", "model": "lora", "link": "https://civitai.com/api/download/models/102047"},
  # {"dn": "Perky_breasts", "type": "quality", "model": "lora", "link": "https://civitai.com/api/download/models/29906"},
  # {"dn": "Frame_binder", "type": "bondage_only", "model": "lora", "link": "https://civitai.com/api/download/models/20798"},
  # {"dn": "pull_Pantyhose", "type": "cloth_legs", "model": "lora", "link": "https://civitai.com/api/download/models/14722"},
  # {"dn": "Guided_Penetration", "type": "pose_for_nude", "model": "lora", "link": "https://civitai.com/api/download/models/24397"},
  # {"dn": "Mechanical_Stationary_Restraints", "type": "bondage_suspension", "model": "lora", "link": "https://civitai.com/api/download/models/21456"},
  # {"dn": "Pantyhose", "type": "cloth_legs", "model": "lora", "link": "https://civitai.com/api/download/models/10212"},
  # {"dn": "Holding_sex", "type": "sex", "model": "lora", "link": "https://civitai.com/api/download/models/125934"},
  # {"dn": "Split_legs", "type": "other_pose", "model": "lora", "link": "https://civitai.com/api/download/models/7141"},
  # {"dn": "All_fours_from_above", "type": "pose_for_nude", "model": "lora", "link": "https://civitai.com/api/download/models/61942"},
  # {"dn": "bondage_and_dildo", "type": "bondage_suspension", "model": "lora", "link": "https://civitai.com/api/download/models/50309"},
  # {"dn": "Kisses", "type": "yuri", "model": "lora", "link": "https://civitai.com/api/download/models/25591"},
  # {"dn": "Sexy_underwear", "type": "cloth_full", "model": "lycon", "link": "https://civitai.com/api/download/models/58572"},
  # {"dn": "Spread_pussy", "type": "pose_for_nude", "model": "lora", "link": "https://civitai.com/api/download/models/74117"},
  # {"dn": "M_Spread_legs", "type": "pose_for_nude", "model": "lora", "link": "https://civitai.com/api/download/models/19696"},
  # {"dn": "Pillory", "type": "bondage_suspension", "model": "lora", "link": "https://civitai.com/api/download/models/111550"},
  # {"dn": "BAstyle_CounterFeitMix", "type": "other-sdcp", "model": "cp", "link": "https://civitai.com/api/download/models/177313"},
  # {"dn": "Cum_on_Tongue", "type": "other_pose", "model": "lora", "link": "https://civitai.com/api/download/models/32600"}
  # {"dn": "Legs_Together_UP", "type": "pose_for_nude", "model": "lora", "link": "https://civitai.com/api/download/models/20873"},
  # {"dn": "Pussy_from_Below", "type": "pose_for_nude", "model": "lora", "link": "https://civitai.com/api/download/models/63354"},
  # {"dn": "hands_in_panties", "type": "pose_for_nude", "model": "lora", "link": "https://civitai.com/api/download/models/170310"},
  # {"dn": "Spread_legs_up", "type": "pose_for_nude", "model": "lora", "link": "https://civitai.com/api/download/models/61649"},
  # {"dn": "Pose_fix_helper", "type": "pose_for_nude", "model": "lora", "link": "https://civitai.com/api/download/models/20974"},
  # {"dn": "Cameltoe", "type": "pose_for_nude", "model": "lora", "link": "https://civitai.com/api/download/models/63536"},
  # {"dn": "Fucked_after_sex", "type": "pose_for_nude", "model": "lycoris", "link": "https://civitai.com/api/download/models/89959"},
  # {"dn": "bed_invitation", "type": "pose_for_nude", "model": "lycoris", "link": "https://civitai.com/api/download/models/41086"},
  # {"dn": "Frogtie_pose", "type": "bondage_only", "model": "lora", "link": "https://civitai.com/api/download/models/175484"},
  # {"dn": "AnyLoraCleanLinearMix_ClearVAE_for_merge", "type": "other-sdcp", "model": "cp", "link": "https://civitai.com/api/download/models/115828"}
  {"dn": "bare_breats", "type": "cloth_breasts", "model": "lora", "link": "https://civitai.com/api/download/models/65126"},
  {"dn": "Naked_Suspender", "type": "cloth_full", "model": "lora", "link": "https://civitai.com/api/download/models/95547"},
  {"dn": "Naked_bandage", "type": "cloth_full", "model": "lora", "link": "https://civitai.com/api/download/models/75300"},
  {"dn": "bodychain", "type": "cloth_full", "model": "lora", "link": "https://civitai.com/api/download/models/25062"},
  {"dn": "thin_round_glasses", "type": "cloth_head", "model": "lora", "link": "https://civitai.com/api/download/models/28564"}
)
"""i: このコードを使用するうえでの変数
Syntax:
Tuple[dict] ..

dict's Syntax:
"dn": "DISPLAY_NAME", "type": "Literal[..]", "model": "Literal[vae, cp, lora, lycoris]", "link": "Optional. Install URL for wget function"}

Requirements:
dn (Display name)
type (Variant)
"""

if __name__ == "__main__":
  n = Main(allow_custom_type=True)
  n.join(i)
  n.start()