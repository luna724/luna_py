import luna_GlobalScript.misc.jsonconfig as jsoncfg

# インプットデータ
input_datas = jsoncfg.read("./config.json")

# Markdownを自動生成する関数
def generate_markdown(input_datas):
    input_data = input_datas
    this_part = 0
    a = ["a","a","a"]
    markdown = ""
    markdown += "| プロンプト | 内容 |\n"
    markdown += "| --- | --- |\n"

    for prompt, content in input_data.items():
        markdown += f"| {prompt} | {content} |\n"

    markdown += "\n<details>\n<summary>サンプル</summary>\n\n"
    markdown += "|"
    
    input_data = input_datas
    this_part_run_count = 0
    this_part = 0

    # ヘッダー行の作成
    tp = 0
    for prompt in input_data.keys():
        if tp == 3:
            tp = 0
            break
        markdown += f" {prompt} |"
        tp += 1

    markdown += "\n|"

    for _ in a:
        markdown += " --- |"
    markdown += "\n|"

    # データ行の作成
    for prompt in input_data.keys():
        if this_part == 3:
            this_part_run_count += 1
            markdown += f"\n| | |\n|"
            # 辞書の1番目から3番目までの内容を別の辞書にコピー
            start_idx = 3 * this_part_run_count
            end_idx = start_idx + 3

            # 辞書のキーをリストとして取得
            keys = list(input_data.keys())

            # 別の辞書にコピーする
            try:
                copied_dict = dict((keys[i], input_data[keys[i]]) for i in range(start_idx, end_idx))
            except IndexError:
                end_idx = min(end_idx, len(keys))
                copied_dict = dict((keys[i], input_data[keys[i]]) for i in range(start_idx, end_idx))

            for prompt in copied_dict.keys():
                markdown += f" {prompt} |"

            markdown += "\n|"
            this_part = 0
        
        markdown += f' <img src="./sample/hair/{prompt}.png" width=80x80> |'
        this_part += 1

    markdown += """\n|\n---\n\n</details>\n\n<details>\n<summary>サンプル画像取得先</summary>\nhttps://e-penguiner.com/hair-prompt-list-for-image-generation-ai/\n</details>\n\n<br>\n"""

    return markdown

# Markdownを生成
generated_markdown = generate_markdown(input_datas)
print(generated_markdown)