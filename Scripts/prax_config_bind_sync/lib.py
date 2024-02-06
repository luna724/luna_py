
def get_binds(basic_data_dict):
  binds4module = []
  
  for x in basic_data_dict["modules"]:
    bind = x["keybind"]
    print("Detected keybind for {x['name']} key: {x['keybind']}")
    
    if bind != 0:
      binds4module.append(bind)
    else:
      binds4module.append(None)
  return binds4module

def get_module_index_from_name(name, target_config):
  for index, data in enumerate(target_config["modules"]):
    if data["name"] == name:
      return index

def set_key_from_index(target_config, index, key)

def reset_keybind(prv_config, db_config, replace, strict):
  bind_list = get_binds(db_config)
  newed_binds = get_binds(prv_config)
  
  for index, bind in enumerate(bind_list):
    if strict:
      if db_config["modules"][index]["name"] != prv_config["modules"][index]["name"]:
        print("not matched module name in ", index, ".\nanalyzing correct module..", end="")
        correctly_index = get_module_index_from_name(db_config["modules"][index]["name"], prv_config)
        