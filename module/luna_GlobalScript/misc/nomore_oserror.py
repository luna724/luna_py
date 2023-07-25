import os
wincannotaddfilename = ["?","/",'"',"\"",":","|","<",">","*"]

def filename_resizer(resize_name, type, replaceTo):
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