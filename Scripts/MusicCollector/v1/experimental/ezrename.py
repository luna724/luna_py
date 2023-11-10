# ファイル名の変更
"""
listfile に取得ファイルのリストを保存
flacの拡張子のみに厳選
-{filename} に当たる位置を x に取得
さらに 0xxx に絞り込み
forループ内で、値に応じたファイル名を取得
ファイル名に応じてリネーム

    """

# import os
# import LGS.misc.re_finder as find
# import LGS.misc.nomore_oserror as los
# import LGS.misc.jsonconfig as jsoncfg
# import LGS.misc.output_folder as of

# dir = of.output(True)

# count = 1
# listfile = os.listdir(dir)
# listfile = los.file_extension_filter(listfile, [".flac"])
# info_dict = jsoncfg.read("./song_info.json")
# os.chdir(dir)

# for file in listfile:
#     x = file.split("-", 1)[-1]
#     x = find.extract(r"(\d+)_\d+\.flac", x)
#     # この先には値に応じてファイル名を変更する機能を実装する
#     # """
    
#     if x is not None and x in info_dict:
#         new_name = info_dict[x]
#         new_name = new_name.replace("\n", "")
        
        
#         while os.path.exists(f"{new_name}.flac"):
#             new_name = f"{new_name} ({count})"
#             count += 1

#         new_name = f"{new_name}.flac"
#         new_name = los.filename_resizer(new_name, replaceTo="_")
#         os.rename(file, new_name)
#         print(f"{file} -> {new_name}")
#     else:
#         print(f"Error: Key {x} not found in info_dict")
    

### 作り直し!!

import LGS.misc.jsonconfig as jsonconfig
import os
import LGS.misc.re_finder as re
import LGS.misc.nomore_oserror as no
import shutil

dir = "./outputs"

# json空読み込み
info_dict = jsonconfig.read("./song_info.json")

# ファイルのリストアップ
filelist = os.listdir(dir)

# 相対パスを使わなくていいように、ディレクトリを変更
os.chdir(dir)

for x in filelist:
    num = 1
    # ファイル名から必要な部分だけ抜き取り
    y = x.split("-", 1)[-1] 
    ans = re.extract(r"(\d+)_\d+\.flac", y)
    print(f"RE Answer: {ans}\n \
        ({x} -> {ans})")

    # 辞書から取得
    dict_data = info_dict[ans]
    
    # ファイル名に含めない文字を除外
    resize_data = no.filename_resizer(dict_data, replaceTo="")
    
    # ファイル名が存在する場合、番号をつける
    while True:
        new_resize_data = resize_data + (f" ({num})" if num > 1 else "") + ".flac"
        if not os.path.exists(new_resize_data):
            break
        num += 1
    
    # 最後に変更    
    new_resize_data = new_resize_data + ".flac"
    new_resize_data = new_resize_data.replace("\n", "")
    shutil.move(x, new_resize_data)