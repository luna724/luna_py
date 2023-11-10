import LGS.misc.jsonconfig as jsoncfg
from LGS.misc.nomore_oserror import filename_resizer

def save(
  filename="cache",
  value="",
  type="txt" # ["txt", "luna", "json", "other.extension (e.g: ".txt", ".log")"]
):
  keyword_type = ["txt", "luna", "json", "none"]
  filename = filename_resizer(filename)
  
  if not type.lower() in keyword_type:
    FILE_EXT = type
    jsoncfg.write_text(
      value, f"./{filename}{FILE_EXT}", overwrite=True
    )
  else:
    if type.lower() == "txt":
      FILE_EXT = ".txt"
      jsoncfg.write_text(
        value, f"./{filename}{FILE_EXT}"
      )
    elif type.lower() == "luna":
      FILE_EXT = ".lunacache"
      # lunacache COMING SOON..
      jsoncfg.write_text(
        value, f"./{filename}{FILE_EXT}", overwrite=False
      )
    elif type.lower() == "json":
      FILE_EXT = ""
      jsoncfg.write(
        value, f"./{filename}.json"
      )
    elif type.lower() == "none":
      FILE_EXT = ""
      jsoncfg.write_text(
        value, f"./{filename}"
      )