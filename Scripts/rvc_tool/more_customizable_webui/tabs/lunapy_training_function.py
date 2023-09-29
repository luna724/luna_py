## set_config(lr, lr_decay, seed)

import json
import os
import random

def file_extension_filter(file_list, allowed_extensions):
    filtered_files = [file for file in file_list if os.path.splitext(file)[1].lower() in allowed_extensions]
    return filtered_files

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
  
def resize_seed(seed):
  if not 0 < seed:
    seeds = -1
  elif seed == -1:
    seeds = -1
  else:
    seeds = seed
  
  if seeds == -1:
    seeds = random.randrange(1, 1000000000)
    
  return seeds
# read target
# ./configs/*.json

def set_config(lr, lrd, seed):
  seeds = resize_seed(seed)
# めんどくさいし、とりあえず全部変更
  filelist = file_extension_filter(os.listdir("./configs/"), [".json"])
  
  for file in filelist:
    datas = read(f"./configs/{file}")
    data = datas["train"]
    
    data["learning_rate"] = float(lr)
    data["lr_decay"] = float(lrd)
    data["seed"] = int(seeds)


    datas["train"] = data
    
    write(datas, f"./configs/{file}")

if __name__ == "__main__":
  os.chdir("..\\")
  set_config(10492, 4291.2941, -4212)