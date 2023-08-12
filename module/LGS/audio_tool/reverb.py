import sox
import librosa
import soundfile as sf

def sox_mode(input_file, rate=35, output=False, output_file=""):
    data, sr = librosa.load(input_file, sr=None)
    
    tfm = sox.Transformer()
    tfm.reverb(rate)
    
    y_reverb = tfm.build_array(input_array=data, sample_rate_in=sr)
    
    if output:
      sf.write(output_file, y_reverb, sr=sr)
    
    return y_reverb, sr
