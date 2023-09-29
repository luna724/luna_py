import cp_dataset as data

sdcp_list = data.cp_list

def generate_table(contents, items_per_row=5):
    table_html = "| Available Information | | | | |\n| --- | --- | --- | --- | --- |\n"
    for index, content in enumerate(contents, start=1):
        table_html += f"| {content} "
        if index % items_per_row == 0:
            table_html += "|\n"
    table_html += "|"
    return table_html
  


def search(text,view_mode=False):
  r_list = []
  print("sdcp_list: ", sdcp_list)
  for s in sdcp_list:
    if text.lower() in s.lower().strip():
      r_list.append(s)
    else:
      continue
  
  if view_mode:
    return r_list
  
  # ないなら
  if len(r_list) < 1:
    return "| Available Information |\n| --- |\n| ### No Match Found |"

  else:
    return generate_table(r_list)
  
def view(searchs):
  print("sdcp_list: ", sdcp_list)
  low = []
  for x in sdcp_list:
    low.append(x.lower())
  
  if not searchs.lower() in low:
    available_ = search(searchs, True)
    if len(available_) == 1:
      view_target = available_[0]
    elif len(available_) < 1:
      view_target = "Error?MODELNOTFOUND"
      print("ERROR: Matching Model Not Found.")
    else:
      print("WARN: Convert Target Model has Not Found.\nSearching Result 2+ Found (Not All Match) Using Index 0")
      view_target = available_[0]
  
  md_up, md_down, md_simply, md_cute, md_rnd, simply_img, cute_img, rnd_img = data.generate(view_target.lower())
  
  
  return md_up, md_simply, simply_img, md_cute, cute_img, md_rnd, rnd_img, md_down
  # md_up
  # 
  # md_simply | simply_img
  # md_cute | cute_img
  # md_rnd | rnd_img
  #
  # md_down
  # return info