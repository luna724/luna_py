import pyaudio
import wave

def wav_32bit(duration, sample_rate, chunk, channels, output_filename):
    # 呼び出し方法
    # example.wav_32bit(録音時間, サンプリングレート, チャンク数, チャンネル, 出力ファイル)
    # 1 = モノラル  |  2 = ステレオを表す
    #
    #　推奨値
    # *, 44100, 1024, 2, ./output.wav
    #
    #duration = 10  # 録音時間（秒）
    #bitrate = 5644  # ビットレート（Kbps）
    #sample_rate = 44100  # サンプリングレート（Hz)
    #chunk = 256
    format = pyaudio.paInt32
    #channels = 1

    audio = pyaudio.PyAudio()

    stream = audio.open(format=format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk)

    frames = []
    for i in range(0, int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(output_filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(format))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))
    wf.close()

    print("録音が完了しました。")