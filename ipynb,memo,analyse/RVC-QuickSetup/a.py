import asyncio
import concurrent.futures
import librosa
import os
import luna_GlobalScript.misc.music_normalizer as normalizer

# ファイルの非同期読み込み関数
async def load_audio(file_path):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(executor, librosa.load, file_path, sr=None)
        audios, srs = await fut
    return audios, srs

# メイン処理
async def main():
    input_dir = "./input_test"  # inputディレクトリのパスを指定してください
    output_dir = "./out"  # 出力ディレクトリのパスを指定してください
    n_mfcc = 13
    hop_length = 512

    # inputディレクトリのファイル一覧を取得
    file_list = os.listdir(input_dir)

    # ファイルごとに非同期に処理
    for file_name in file_list:
        # ファイルのパスを作成
        file_path = os.path.join(input_dir, file_name)

        # 非同期にファイルを読み込み
        audios, srs = await load_audio(file_path)
        print("Success Loading")

        # MFCCの抽出
        mfcc = librosa.feature.mfcc(audios, sr=srs, n_mfcc=n_mfcc, hop_length=hop_length)
        print("Success MFCC Extract")

        # 正則化
        normalized_mfcc = normalizer.normalize(mfcc)
        print("Success Normalized")

        # 出力パスの作成
        output_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}_normalizer.mp3")

        # 出力処理
        librosa.output.write_mp3(output_path, normalized_mfcc, srs)
        print("Success Saving")

# メイン処理の非同期実行
asyncio.run(main())
