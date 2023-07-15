import luna_GlobalScript.music_file.record_highOption as record
import random

num = random.randrange(1,200) * random.randrange(1,200)

num += random.randrange(1, 2000)
out_n = f"./out/wav_outputs_{num}.wav"        # ファイル名の設定
record.wav_32bit(12,44100,256,2,out_n)