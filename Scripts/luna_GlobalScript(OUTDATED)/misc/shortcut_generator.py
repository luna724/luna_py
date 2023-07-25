import winshell
import os

def create_shortcut(target_file, shortcut_name, custom_folder_path):
    folder_path = custom_folder_path  # 任意のフォルダーパスを指定
    path = os.path.join(folder_path, shortcut_name)
    with winshell.shortcut(path) as shortcut:
        shortcut.path = target_file
        shortcut.write()