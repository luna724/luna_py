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
       
    return markdown


x = generate_markdown(input_datas)
print(x)