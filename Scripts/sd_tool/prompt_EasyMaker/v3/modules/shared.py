import os

ROOT_DIR = os.getcwd()
negative = "EasyNegative, badhandv5, (((1boy))), (bad anatomy:1.4), (realistic:1.1), (low quality, worst quality:1.1), lips, fat, (inaccurate limb:1.2), (Low resolution:1.1)"
ad_pos = "masterpiece, best quality,"
ad_neg = "worst quality, (EasyNegative:0.725)"

delete_cache = False


# Template Prompt System
currently_version = "v3"
currently_template_versionID = 2 # v3-r5 - 3.0.2
noneimg = os.path.join(ROOT_DIR, "database", "v3", "noneimg8cmwsvcifvfosi923jrvsvvnsfs.png")

class script_data():
  class modules_generate():
    acceptable_version = ["v3", "v4β"]
    
  generate_py = modules_generate()
  

data = script_data()