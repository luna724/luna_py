import os

def delete_small_png_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(".png"):
            if os.path.getsize(filepath) < 1024:  # ファイルサイズが1KB未満の場合
                os.remove(filepath)
                print(f"Deleted: {filename}")

# 特定のディレクトリを指定して実行
target_directory = "./out/minori"
delete_small_png_files(target_directory)
