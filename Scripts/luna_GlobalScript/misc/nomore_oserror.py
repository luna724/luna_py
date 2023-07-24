wincannotaddfilename = ["?","/",'"',"\"",":","|","<",">","*"]

def filename_resizer(resize_name, type, replaceTo):
    configname = resize_name
    if replaceTo == "":
        replaceTo = "_"
    if type == "filename":
        for x in wincannotaddfilename:
            configname = configname.replace(x, replaceTo)
    
    return configname