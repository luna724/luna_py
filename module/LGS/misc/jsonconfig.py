import json

def read(filepath, encode: str = "utf-8", silent=False):
    if not silent:
        print("Reading jsondata..")
    with open(filepath, 'r', encoding=encode) as file:
        data = json.load(file)
    return data

def write(data, filepath, encode: str = "utf-8", silent=False): 
    if not silent:
        print("Writing config to jsondata..")
    with open(filepath, 'w', encoding=encode) as file:
        json.dump(data, file, indent=4)  # indent=4でフォーマットを整形して書き込み
    return data

def read_text(filename: str, 
                strip_mode: DeprecationWarning("") = None):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

def write_text(data, filepath="./out.txt", overwrite=True, encode:str = "utf-8"):
    if overwrite:
        with open(filepath, "w", encoding=encode) as f:
            f.write(data)
    
    else:
        with open(filepath, "a", encoding=encode) as f:
            f.write(data)