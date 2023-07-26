import librosa
import soundfile as sf
import numpy as np
import subprocess

def librosa_mode(input_file, noise_strength=0.1, output=False, output_file=""):
    #input_file = "input.wav"
    #output_file = "output_with_noise.wav"
    #noise_strength = 0.1  # ホワイトノイズの強さ（0から1の範囲）
    y, sr = librosa.load(input_file, sr=None)
    noise = np.random.randn(len(y))
    y_with_noise = y + noise_strength * noise
    if output:
        sf.write(output_file, y_with_noise, sr)
    
    
    return y_with_noise, sr


def sox_mode(input_file, noise_data, output_file, waiting=True):
    if waiting:
        process_handle = subprocess.Popen(
      ["sox", input_file, noise_data, output_file, "mix", str(1), str(1)]
      , stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        process_handle.communicate()
        
    else:
        subprocess.run(["sox", input_file, noise_data, output_file, "mix", str(1), str(1)])
