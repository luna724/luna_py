import luna_GlobalScript.misc.jsonconfig as jsoncfg

def read_text_file(filename, splitting="\t"):
    input_data = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                prompt, details = line.split(splitting)  # 全角空白で分割
                input_data[prompt] = details
    return input_data

x = input("区切り文字を入力(タブの場合未入力): ")
if x == "":
    input_data = read_text_file("./input_HERE.txt")
else:
    input_data = read_text_file("./input_HERE.txt", x)


jsoncfg.write(input_data, "./config.json")