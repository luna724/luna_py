from pydub import AudioSegment
import librosa
import soundfile as sf
import subprocess

#input_file = "input.wav"
#output_file = "output_time_shift.wav"
#time_shift_ms = 500  # シフトする時間（ミリ秒）

def pydub_mode(input_file, time_shift_ms=500, output=False, output_file="", format="wav"):
    sound = AudioSegment.from_file(input_file)
    new_sound = sound._spawn(sound.raw_data, overrides={
        "frame_position": int(time_shift_ms * sound.frame_rate / 1000)
    })
    new_sound.export(output_file, format="wav")


# time_shift_factor = 0.5  # 時間シフトの変更率
def librosa_mode(input_file, time_shift_factor=0.3, output=False, output_file=""):
    y, sr = librosa.load(input_file, sr=None)
    y_time_shift = librosa.effects.time_stretch(y, time_shift_factor)
    
    if output:
        sf.write(output_file, y_time_shift, sr)
        
    return y_time_shift, sr


def sox_mode(input_file, time_shift_factor, output_file, waiting=True, return_output=False):
    if waiting:
        process_handle = subprocess.Popen(
            ["sox", input_file, output_file, "speed", str(time_shift_factor)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        process_handle.communicate()
    
    else:
        subprocess.run(["sox", input_file, output_file, "speed", str(time_shift_factor)])
    
    if return_output:
        return output_file