import math, json

def normalize_input(
  batch_size, 
  epochs,
  max_index_size,
  f0ing,
  gpu_id
  ):
  batch_size = int(batch_size)
  epochs = int(epochs)
  max_index_size = int(max_index_size)
  f0 = f0ing
  gpu_ids = [int(x.strip()) for x in gpu_id.split(",")] if gpu_id else []
  
  SR_DICT = {
    "32k": 32000,
    "40k": 40000,
    "48k": 48000,
  }
  
  return SR_DICT, batch_size, epochs, max_index_size, f0, gpu_ids
