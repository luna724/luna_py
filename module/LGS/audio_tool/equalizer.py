import sox
import librosa
import soundfile as sf

def sox_mode(input_file, Hzeq=100, gain=1.5, q=5.0, output=False, output_file=""):
    data, sr = librosa.load(input_file, sr=None)
    
    tfm = sox.Transformer()
    # freq = random.uniform(100, 2000)  # ランダムな周波数
    # gain = random.uniform(1.0, 3.0)   # ランダムな増幅率
    # q = random.uniform(1.0, 10.0)     # ランダムなQ値
    tfm.equalizer(Hzeq, gain, q)
    
    y_eq = tfm.build_array(input_array=data, sample_rate_in=sr)
    
    if output:
      sf.write(output_file, y_eq, sr=sr)
    
    return y_eq, sr