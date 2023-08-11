import LGS.misc.debug_tool as dt
Debug_Mode = True

def dprint(str):
  if Debug_Mode:
    dt.dprint(str)

augment_list = \
[{"1": "type_noise"}, {"2": "pitch_shift"}]
noise_type_list = \
["white_noise", "pink_noise", "brown_noise"]

# 関数
from pydub import AudioSegment
import subprocess

# ピッチ変換関数 (pydub)
def pitch_change_relative(input_file, output_file, ratio):
    sound = AudioSegment.from_file(input_file)
    frame_rate = sound.frame_rate  # サンプリングレートを取得
    target_frame_rate = int(frame_rate * ratio)  # 元サンプリングレートに対する倍率で変更
    sound_changed = sound.set_frame_rate(target_frame_rate)  # サンプリングレートを変更
    sound_changed.export(output_file, format="wav")
    
    
def volume_change_relative(input_file, output_file, ratio):
    sound = AudioSegment.from_file(input_file)
    default_volume = sound.dBFS  # 元の音量（デフォルト値）をdBFSで取得
    target_volume = default_volume * ratio  # デフォルト音量に対する倍率で変更
    sound_changed = sound + target_volume  # ボリュームを変更
    sound_changed.export(output_file, format="wav")


# タイムシフト関数
def time_shift(input_file, output_file, shift_ms):
    sound = AudioSegment.from_file(input_file)
    sound_shifted = sound._spawn(b'\x00' * shift_ms + sound.raw_data)
    sound_shifted.export(output_file, format="wav")
    
    
# ホワイトノイズ追加関数 (SoX)
def add_white_noise(input_file, output_file, strength):
    subprocess.run(["sox", input_file, output_file, "synth", "whitenoise", "amplitude", str(strength)])
    
  
# メイン!
def augment(date_dict_____):
  for date in date_dict_____.values():
    augment_type = []
    IN_FORMAT = date[0]["format"]
    augment_raw = date[0]["augment"]
    ID = date[0]["ID"]
    DEFAULT_NAME = date[0]["NAME"]

    # 1番目リストから辞書に
    augment_raw_dict = augment_raw[0]
    
    # 拡張のタイプを取得
    augment_id_list = list(augment_raw_dict.keys())
    
    # "1" (ノイズ) が含まれる場合、ノイズタイプを取得
    if "1" in augment_id_list:
      augment_noise_type = augment_raw_dict["1"]
    
    # HR(Human Readable)に変換
    for x in augment_id_list:
      if x == "1":
        normalize = augment_noise_type
        augment_type.append(normalize)
        continue
      
      augment_type.append(augment_raw_dict[x])
    
    # 2番目があるなら、2番目
    if len(augment_raw) > 1:
      augment_raw_dict = augment_raw[1]
       # 拡張のタイプを取得
      augment_id_list = list(augment_raw_dict.keys())
      
      # "1" (ノイズ) が含まれる場合、ノイズタイプを取得
      if "1" in augment_id_list:
        augment_noise_type = augment_raw_dict["1"]
      
      # HR(Human Readable)に変換
      for x in augment_id_list:
        if x == "1":
          normalize = augment_noise_type
          augment_type.append(normalize)
          continue
        
        augment_type.append(augment_raw_dict[x])
      
          # 3番目があるなら、3番目
    if len(augment_raw) > 2:
      augment_raw_dict = augment_raw[2]
       # 拡張のタイプを取得
      augment_id_list = list(augment_raw_dict.keys())
      
      # "1" (ノイズ) が含まれる場合、ノイズタイプを取得
      if "1" in augment_id_list:
        augment_noise_type = augment_raw_dict["1"]
      
      # HR(Human Readable)に変換
      for x in augment_id_list:
        if x == "1":
          normalize = augment_noise_type
          augment_type.append(normalize)
          continue
        
        augment_type.append(augment_raw_dict[x])
    # テスト!
    dprint(f"Return: \n\
IN_FORMAT = {IN_FORMAT}  |  ID = {ID}  |  DEFAULT_NAME = {DEFAULT_NAME}\n\
augment_id_list = {augment_id_list}\n\
HR_augment_list = {augment_type}")
    
    # データ形式
    # Debug: Return:
    # IN_FORMAT = .wav  |  ID = 0001  |  DEFAULT_NAME = 5_STAGE OF SEKAI-full-望月 穂波+星乃 一歌+鏡音 レン+天馬 咲希+日野森  志歩_(Vocals) ichika
    # augment_id_list = ['2']
    # HM_augment_list = ['brown_noise', 'pitch_shift']
    
    # augment_listに応じて、関数形式を設定
    