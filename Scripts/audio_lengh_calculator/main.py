from pydub import AudioSegment
from pydub.silence import split_on_silence

def calculate_audio_duration_without_silence(audio_path, silence_threshold=-50, silence_min_length=700):
    sound = AudioSegment.from_file(audio_path)
    chunks = split_on_silence(sound, silence_thresh=silence_threshold, min_silence_len=silence_min_length)
    
    total_duration_without_silence = sum([len(chunk) for chunk in chunks])
    return total_duration_without_silence / 1000  # Convert milliseconds to seconds

# if __name__ == "__main__":
#     audio_path = "path/to/your/audio/file.mp3"
#     duration_without_silence = calculate_audio_duration_without_silence(audio_path)
#     print(f"Duration without silence: {duration_without_silence:.2f} seconds")

import LGS.misc.nomore_oserror as los
import LGS.misc.random_roll as roll
import os
import time
import shutil

def advanced_main(target_path, silence, date):
  split_ms = date["SplitAfter"]
  output_dir = date["Output"]
  chance = date["Activate_chance"]
  
  split_s = split_ms // 1000
  
  files = los.file_extension_filter(os.listdir(target_path), [".mp3", ".wav", ".flac", ".aiff"])
  
  total_duration = 0
  file_added = 0
  
  while not int(total_duration) > int(split_s):
    for file in files:
      # 確率で無視
      if roll.random_roll(chance):
        continue
      
      file_path = os.path.join(target_path, file)
      duration = calculate_audio_duration_without_silence(file_path, silence_min_length=silence)
      
      print(f"Return Duration: {duration}")
      total_duration += duration
      file_added += 1
      
      if int(total_duration) > int(split_s):
        break
      
      else:
        shutil.copy(file_path, os.path.join(output_dir, file))
  
  
  
  return True, file_added

def main(target_path, ignore_silence_time=1000, advanced={"Advanced" : False}):
  #     Advanced_dict = {"Advanced" : Advanced,
#                     "SplitAfter": split_after,
#                     "Output": d,
#                     "Activate_chance": activate_chance
#                     }
  files = los.file_extension_filter(os.listdir(target_path), [".mp3", ".wav", ".flac"])
  
  if advanced["Advanced"] == True:
    r, rf = advanced_main(target_path, ignore_silence_time, advanced)
    return r, rf

  total_duration = 0
  for file in files:
    file_path = os.path.join(target_path, file)
    duration = calculate_audio_duration_without_silence(file_path, silence_min_length=ignore_silence_time)
    print(f"Return Duration: {duration}")
    
    total_duration += duration
    
    time.sleep(0.25)
    
  
  return total_duration, len(files)