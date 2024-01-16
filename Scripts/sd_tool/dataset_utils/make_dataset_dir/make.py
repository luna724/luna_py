import os
from shared import BASE_DIR, isColab
from os import makedirs as mkdr
from LGS.misc.nomore_oserror import filename_resizer

def makedir(name: str ="", version: str ="v1.0"):
  name = filename_resizer(name, replaceTo="_")
  os.makedirs(name, exist_ok=True)
  os.makedirs(
    os.path.join(name, version), exist_ok=True
  )
  os.makedirs(
    os.path.join(name, version, "dataset_raw"), exist_ok=True
  )
  os.makedirs(
    os.path.join(name, version, "dataset_raw", "processed"), exist_ok=True
  )
  os.makedirs(
    os.path.join(name, version, "dataset_preprocessing_p1"), exist_ok=True
  )
  os.makedirs(
    os.path.join(name, version, "dataset_preprocessing_p1", "have_background") ,exist_ok=True
  )
  os.makedirs(
    os.path.join(name, version, "dataset_preprocessing_p2"), exist_ok=True
  )
  
  return os.path.join(os.getcwd(), name, version)

def main(name, version, targetPath):
  