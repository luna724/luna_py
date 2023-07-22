# 例として、input_dataという辞書があるとします
input_data = {
    "prompt1": "content1",
    "prompt2": "content2",
    "prompt3": "content3",
    "prompt4": "content4",
    "prompt5": "content5",
    "prompt6": "content6"
}

# 辞書の1番目から3番目までの内容を別の辞書にコピー
start_idx = 0  # コピーを開始するインデックス
end_idx = 3    # コピーを終了するインデックス (終了インデックス自体は含まれない)

# 辞書のキーをリストとして取得
keys = list(input_data.keys())

# 別の辞書にコピーする
copied_dict = dict((keys[i], input_data[keys[i]]))

# 結果を表示
print(copied_dict)