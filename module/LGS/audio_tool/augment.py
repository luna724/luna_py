import LGS.misc.debug_tool as dt
import os
import soundfile as sf
import LGS.audio_tool.pitch_shift as pitch_shift
import LGS.audio_tool.white_noise as white_noise
import LGS.misc.random_roll as roll
import random
import LGS.audio_tool.time_shift as time_shifts
import librosa
import LGS.audio_tool.volume_exchange as volume_exchange
import LGS.audio_tool.equalizer as eqs
import LGS.audio_tool.reverb as reverb
import time 

Debug_Mode = True

def dprint(str):
  if Debug_Mode:
    dt.dprint(str)


noise_type_list = \
["white_noise", 
 #"pink_noise", "brown_noise"
 ]

# 関数
# 変換値設定関数
def randoms(min, max, float_range=6, load_config=False, load_from=""):
  #value = random.randrange(min, max)
  value = round(random.uniform(min, max), float_range)
  return value


# ピッチ変換関数 (librosa)
def pitch_change_relative(input_file):
    # ratioを自動設定
    ratio = randoms(0.96, 1.05)
    audio, sr = pitch_shift.librosa_mode(input_file=input_file, pitch_factor=ratio)
    return audio, True, sr
    # sound = AudioSegment.from_file(input_file)
    # frame_rate = sound.frame_rate  # サンプリングレートを取得
    # target_frame_rate = int(frame_rate * ratio)  # 元サンプリングレートに対する倍率で変更
    # sound_changed = sound.set_frame_rate(target_frame_rate)  # サンプリングレートを変更
    # sound_changed.export(output_file, format="wav")
    
# ボリューム変換 (pydub)
def volume_change_relative(input_file):
  # volume_factor の設定
  vol_factor = randoms(1.001, 1.25, 4)
  audio, sr = volume_exchange.librosa_mode(input_file=input_file, volume_factor=vol_factor)

  return audio, True, sr

# タイムシフト関数
def time_shift(input_file):
  # time_shift_factor の計算
  y, sr = librosa.load(input_file, sr=None)
  duration = librosa.get_duration(y=y, sr=sr) 
  audio_mstime = duration * 1000
  time_shift_factor = audio_mstime * round(random.uniform(0.5, 0.7), 4)
  print(f"time_shift_factor: {time_shift_factor}")
  print(f"y shape: {duration} ")
  audio, sr = time_shifts.numpy_mode(input_file=input_file, time_shift_factor=int(time_shift_factor))
  
  return audio, False, sr
    # sound = AudioSegment.from_file(input_file)
    # sound_shifted = sound._spawn(b'\x00' * shift_ms + sound.raw_data)
    # sound_shifted.export(output_file, format="wav")
    
    
# ホワイトノイズ追加関数 (librosa)
def add_white_noise(input_file):
  strength = randoms(0.0001, 0.015, 4)
  audio, sr = white_noise.librosa_mode(input_file=input_file, noise_strength=strength)
  return audio, True, sr
    
# イコライザ適用
def eq(input_file):
  # いろいろと設定
  Hzeqs = randoms(100, 4000, 2)
  gains = randoms(1.0, 3.0, 1)
  qs = randoms(1.0, 10.0, 2)
  
  audio, sr = eqs.sox_mode(input_file, Hzeqs, gains, qs)

  return audio, False, sr

# リバーブ適用
def reverbs(input_file):
  # 値設定
  rate = randoms(30, 40, 1)
  
  audio, sr = reverb.sox_mode(input_file=input_file, rate=rate)
  
  return audio, False, sr


# データ 
augment_list = \
[{"1": "type_noise"}, {"2": "pitch_shift"}, 
 # {"3": "time_shift"}, 
 {"4": "volume_change"},
 {"5": "equalizer"}, {"6": "reverb"}]
augment_list_dict = \
{"white_noise": add_white_noise, 
 "pitch_shift": pitch_change_relative,
 # "time_shift": time_shift,
 "volume_change": volume_change_relative,
 "equalizer": eq,
 "reverb": reverbs}

# メイン!
def augment(date_dict_____, automode, out_format):
  INPUT_DIRECTORY = date_dict_____["Target_Directory_INFO"]
  OUTPUT_DIRECTORY = date_dict_____["Target_Directory_OUT"]
  # 用済みだから消す
  del date_dict_____["Target_Directory_INFO"]
  del date_dict_____["Target_Directory_OUT"]
  
  for date in date_dict_____.values():
    if not "augment" in date[0]:
      continue
    
    augment_type = []
    dprint(f"{date}")
    IN_FORMAT = date[0]["format"]
    augment_raw = date[0]["augment"]
    ID = date[0]["ID"]
    DEFAULT_NAME = date[0]["NAME"]
    OUT_FORMAT = out_format
    OUT_FORMAT_AUTO_DETECTION = automode

    # 移動  
    os.chdir(INPUT_DIRECTORY)
    
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
    # インプット名の設定
    INPUT = f"{DEFAULT_NAME}{IN_FORMAT}"
    OUTPUT = f"{ID}_{DEFAULT_NAME}.{IN_FORMAT}.{OUT_FORMAT}"
    # 出力フォーマット自動検出
    if OUT_FORMAT_AUTO_DETECTION:
      OUTPUT = f"{ID}_{DEFAULT_NAME}_Augmented.{IN_FORMAT}"
      OUT_FORMAT = IN_FORMAT 
    
    # 拡張済みデータを受け取る
    for aug in augment_type:
      os.chdir(INPUT_DIRECTORY)
      time.sleep(1)
      OUTPUT_DATE, use_librosa, DATE_SR = augment_list_dict[aug](INPUT)

      normalizer = False
      # 正則化 + 音量修正 (librosa)
      if roll.random_roll(0.5):
        data_norm = librosa.util.normalize(OUTPUT_DATE)
        normalizer = True
        
      if use_librosa: # 最後には OUT_DATE に集結させる
        if normalizer:
          OUT_DATE = data_norm * 2.0
        else:
          OUT_DATE = OUTPUT_DATE * 2.0
      
      else:
        if normalizer:
          OUT_DATE = data_norm
        
        else:
          OUT_DATE = OUTPUT_DATE
      
      # メッセージ + ファイルへの書き込み
      print(f"\
File Augmented: {DEFAULT_NAME} \n\
Config: \n\
Format: {IN_FORMAT} -> {OUT_FORMAT}\n\
Augment Type: {aug}\n\
Output Directory: {OUTPUT_DIRECTORY}\n\
Output Name: {aug}-{OUTPUT}")
      
      # 書き込み
      os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
      os.chdir(OUTPUT_DIRECTORY)
      
      sf.write(f"./{aug}-{OUTPUT}", OUT_DATE, samplerate=DATE_SR)
      
      