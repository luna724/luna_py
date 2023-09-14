import os
import shutil

def launch(target_root_directory):
  # root -> content
  # /root
  content_list = os.listdir(target_root_directory)
  os.chdir(target_root_directory)
  
  for content in content_list:
    # content -> outputs
    # /root/20200301/
    os.chdir(f"./{content}")
    root_path = os.getcwd()
    os.makedirs("./grids", exist_ok=True)
    os.chdir("./grids")
    grids_path = os.getcwd()
    os.chdir("..\\")
    os.chdir("./outputs")
    
    # outputs -> txt2img-grids
    in_list = os.listdir()
    
    for img_in in in_list:
      os.chdir(f"./{img_in}")
      if img_in in "grid":
        this_grid = True
      else:
        this_grid = False
      
      date_list = os.listdir()
      
      for date in date_list:
        # txt2img-grids -> 2020-03-01
        os.chdir(f"./{date}")
        
        # 2020-03-01/*.png -> /root/20200301/grids/*.png
        fullpath = os.getcwd()
        file_list = os.listdir()
        
        for file in file_list:
          filepath = os.path.join(fullpath, file)
          
          if this_grid:
            shutil.copy(filepath, grids_path)
            
          else:
            shutil.copy(filepath, root_path)
            
if __name__ == "__main__":
  a = input("Target Directory: ")
  
  launch(a)