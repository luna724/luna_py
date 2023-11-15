# db_lora_generate.click(
#           fn=dbs.lora_data.save,
#           inputs=[
#             db_lora_name, db_lora_trigger_lora, db_lora_trigger_word,
#             db_lora_optional_word, db_lora_force_update],
#           outputs=[db_lora_status]
#         )

import lib as data
from lib import jsoncfg

class lora_data():
  def save(self, name, ch_lora, ch_name, ch_prompt, force_update):
    lora_dict = {
      name: [ch_lora, ch_name]
    }
    chpr_dict = {
      name: ch_prompt
    }
    
    previous_lora_dict = jsoncfg.read("./database/charactor_lora.json")
    previous_chpr_dict = jsoncfg.read("./database/charactor_prompt.json")
    
    if not force_update:
      if name in previous_lora_dict.keys() and name in previous_chpr_dict.keys():
        return "Failed. stderr: this name is already taken."
      else:
        previous_lora_dict.update(lora_dict)
        previous_chpr_dict.update(chpr_dict)
    else:
      previous_lora_dict.update(lora_dict)
      previous_chpr_dict.update(chpr_dict)
    
    jsoncfg.write(previous_lora_dict, "./database/charactor_lora.json")
    jsoncfg.write(previous_chpr_dict, "./database/charactor_prompt.json")
    
    return "Success! Reload the UI Will add it to generation mode tabs!"

  def load(self, name):
    previous_lora_dict = jsoncfg.read("./database/charactor_lora.json")
    previous_chpr_dict = jsoncfg.read("./database/charactor_prompt.json")
    
    if name in previous_lora_dict.keys() and name in previous_chpr_dict.keys():
      lora = previous_lora_dict
      chpr = previous_chpr_dict
      try:
        ch_lora = lora[name][0]
        ch_name = lora[name][1]
        ch_prompt = chpr[name]
      except IndexError as e:
        print(f"Exception: IndexError (/py/database_setup.py)\nstderr: {e}")
        return name, "", "", "", "", "Failed. stderr: IndexError  loradata database is corrupted?"
      except KeyError as e:
        print(f"Exception: KeyError (/py/database_setup.py)\nstderr: {e}")
        return name, "", "", "", "", "Failed. stderr: KeyError  why is keyerror? i'm already checked a loradata keys. that's unknown exception!"
      return name, ch_lora, ch_name, ch_prompt, "Done!"
      
    else:
      return name, "", "", "", "", "Failed. stderr: loradata Not found. that key are not defined."
    