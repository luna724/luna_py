# インプットデータ
input_datas = {
    "smile": "微笑む",
    "wink": "ウィンク",
    "happy": "幸せそうな顔",
    "laugh": "笑う"
    # 他のインプットがある場合はここに追加する
}

# Markdownを自動生成する関数
def generate_markdown(input_datas):
    input_data = input_datas
    this_part = 0
    markdown = ""
    markdown += "| プロンプト | 内容 |\n"
    markdown += "| --- | --- |\n"

    for prompt, content in input_data.items():
        markdown += f"| {prompt} | {content} |\n"

    markdown += "\n<details>\n<summary>サンプル</summary>\n\n"
    markdown += "|"
    for prompt in input_data.keys():
        markdown += f" {prompt} |"
    markdown += "\n|"
    for _ in input_data.keys():
        markdown += " --- |"
    markdown += "\n"
    for prompt in input_data.keys():
        if this_part == 3:
            this_part_run_count += 1
            markdown += f"\n| | |\n|"
            # 辞書の1番目から3番目までの内容を別の辞書にコピー
            start_idx = 3 * this_part_run_count -1  # コピーを開始するインデックス
            end_idx = start_idx + 3   # コピーを終了するインデックス (終了インデックス自)

            # 辞書のキーをリストとして取得
            keys = list(input_data.keys())

            # 別の辞書にコピーする
            copied_dict = dict((keys[i], input_data[keys[i]]) for i in range(start_idx, end_idx))
            for prompt in input_data.keys():
                markdown += f" {prompt} |"
            markdown += "\n"
            this_part = 0
        markdown += f"| <img src=./sample/facal_expression/{prompt}.png width=80x80> |"
        this_part += 1
    markdown += "\n|\n---\n\n</details>\n\n<details>\n<summary>サンプル画像取得先</summary>\n(取得先のURLやモデル)\n</details>\n\n<br>\n"

    return markdown

# Markdownを生成
generated_markdown = generate_markdown(input_datas)
print(generated_markdown)