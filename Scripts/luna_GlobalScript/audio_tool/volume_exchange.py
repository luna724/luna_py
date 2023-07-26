from pydub import AudioSegment
import librosa
import soundfile as sf
import subprocess

# input_file = "input.wav"
# output_file = "output_volume.wav"
# volume_factor = 0.5  # ボリュームの変更率（0から1の範囲）

def pydub_mode(input_file, volume_factor=1.0, output=False, output_file="", format="wav"):
    sound = AudioSegment.from_file(input_file)
    new_sound = sound - (sound.max * (1 - volume_factor))
    if output:
        new_sound.export(output_file, format=format)

    return new_sound


def librosa_mode(input_file, volume_factor=1.0, output=False, output_file="2"):
    y, sr = librosa.load(input_file, sr=None)
    y_volume = y * volume_factor
    if output:
        sf.write(output_file, y_volume, sr)

    return y_volume, sr


def sox_mode(input_file, volume_factor=1.0, output_file="", return_output=False):
    subprocess.run(["sox", input_file, output_file, "vol", str(volume_factor)])

    if return_output:
        return output_file