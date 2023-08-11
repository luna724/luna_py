import json

def read(filepath):
    print("Reading jsondata..")
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def write(data, filepath): 
    print("Writing config to jsondata..")
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)  # indent=4でフォーマットを整形して書き込み
    return data

def read_text(filename, strip_mode=True):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if strip_mode:
                line = line.strip()
    return line

def write_text(data, filepath="./out.txt", overwrite=True):
    if overwrite:
        with open(filepath, "w") as f:
            f.write(data)
    
    else:
        with open(filepath, "a") as f:
            f.write(data)