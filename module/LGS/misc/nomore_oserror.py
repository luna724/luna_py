import os
wincannotaddfilename = ["?","/",'"',"\"",":","|","<",">","*"]

def filename_resizer(resize_name, type="filename", replaceTo=""):
    configname = resize_name
    if replaceTo == "":
        replaceTo = "_"
    if type == "filename":
        for x in wincannotaddfilename:
            configname = configname.replace(x, replaceTo)
    
    return configname

def file_extension_filter(file_list, allowed_extensions):
    filtered_files = [file for file in file_list if os.path.splitext(file)[1].lower() in allowed_extensions]
    return filtered_files


def nest_listfile(path, isloop=False, relative=""):
    def append(item, lists):
        print("Debug: File Appended! ({})".format(item))
        lists.append(item)
        return lists
    # 初期化
    filelist = []
    
    # path内のアイテムでいろいろする
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            if isloop:
                filelist = (f"./{relative}/{item}", filelist)
            else:
                filelist = (item, filelist)
        # フォルダなら
        elif os.path.isdir(item_path):
            # もう一度実行して追加する
            for x in nest_listfile(item_path, True, item): 
                filelist = append(x, filelist)
    
    return filelist