from pydub import AudioSegment
import librosa
import soundfile as sf
import subprocess

# input_file = "input.mp3"
# output_file = "output_pitch.wav"
# pitch_factor = 1.5  # ピッチの変更率

def pydub_mode(input_file, pitch_factor=1.0, output=False, format="wav", output_file=""):
    sound = AudioSegment.from_file(input_file) # 読み込み
    new_sound = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * pitch_factor)
    }) # Pitch shift
    # エクスポート設定の場合
    if output:
        new_sound.export(output_file, format=format)

    return new_sound


def librosa_mode(input_file, pitch_factor=1.0, output=False, output_file=""):
    y, sr = librosa.load(input_file, sr=None)
    y_pitch = librosa.effects.pitch_shift(y, sr=sr, n_steps=pitch_factor)
    
    if output:
        sf.write(output_file, y_pitch, sr)

    return y_pitch, sr


def sox_mode(input_file, pitch_factor=1.0, output_file="", return_output=False):
    subprocess.run(["sox", input_file, output_file, "pitch", str(pitch_factor)])
    
    if return_output:
        return output_file