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
            markdown += f"\n| | |\n|"
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