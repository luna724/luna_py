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