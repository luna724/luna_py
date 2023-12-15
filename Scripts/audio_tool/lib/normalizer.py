import os
import librosa
import numpy as np
import soundfile as sf
from tqdm import tqdm
from LGS.misc.nomore_oserror import file_extension_filter

def webui(target, convert_all, output_format):
  if output_format == "Keep Previous Format":
    out_format = ""
  else:
    out_format = output_format
    
  if not os.path.exists(target):
    return f"Target Directory / File cannot found."
    
  if convert_all:
    if not os.path.isdir(target):
      return "stderr: Target Directory is not directory (Convert ALL)"
    
    target_file = file_extension_filter(os.listdir(target), [".mp3", ".wav", ".flac"])
    
    session = 0
    total_session = len(target_file)
    for file in tqdm(target_file, desc="Processing with ConvertAll..\n"):
      session += 1
      yield f"Processing with ConvertAll.. ({session}/{total_session})"
      path = os.path.join(target, file)

      if os.path.exists(path):
        audio, sr = librosa.load(path, sr=44100, mono=False)
        norm_audio = np.column_stack([
        librosa.util.normalize(channel) for channel in audio.T
    ])
        
        os.makedirs(os.path.join(target, "lunapy_outputs"), exist_ok=True)
        filename = f"normalized_{file}{out_format}"
        sf.write(os.path.join(target, "lunapy_outputs", filename), norm_audio, sr)
      
  else:
    if not os.path.isfile(target):
      return "stderr: Target Audio file is directory (Single Mode)"
    
    if not os.path.splitext(os.path.basename(target))[1].lower() in [".mp3", ".flac", ".wav"]:
      return f"stderr: can't input file: Unsupported Extension ({os.path.splitext(target)[1].lower()})"
    
    yield f"Processing.."
    
    audio, sr = librosa.load(target, sr=44100, mono=True)
    norm_audio = librosa.util.normalize(audio)

    target_dir = target.replace(
      os.path.basename(target), ""
    )
    
    os.makedirs(os.path.join(target_dir, "lunapy_outputs"), exist_ok=True)
    filename = f"normalized_{os.path.basename(target)}{out_format}"
    sf.write(os.path.join(target_dir, "lunapy_outputs", filename), norm_audio, sr)
      
  return "All Process are Successfully Completed."