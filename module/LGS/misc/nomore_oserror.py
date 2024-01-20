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


def get_nested_files(root_dir, endswith):
    file_list = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(endswith):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, root_dir)
                file_list.append((file_path, relative_path))
    return file_list