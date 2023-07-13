import subprocess

print("利用可能: 1. mp3 -> wav \n2. wav -> mp3  \n3. ogg -> wav \n4. flac -> wav \n5. wav -> flac  |")
mode = int(input("変換モードを選択(番号指定): "))

mode %= 1 
if 0 < mode < 6:
    if mode == 1:
        mode = "mp32wav"
    elif mode == 2:
        mode = "wav2mp3"
    elif mode == 3:
        mode = "ogg2wav"
    elif mode == 4:
        mode = "flac2wav"
    elif mode == 5:
        mode = "wav2flac"
    
    subprocess.run(f'python main.py "{mode}"')