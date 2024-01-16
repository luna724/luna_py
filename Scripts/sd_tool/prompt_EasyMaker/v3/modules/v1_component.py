import re

def delete_duplicate_comma(p):
  while p.count(", , ") > 0:
    p = p.replace(", , ", ", ")
  
  return p

def get_loraweight(prompt: str):
  if not "%LORA:" in prompt:
    return prompt, "%LORA%"

  pattern = r"%LORA:(\d+\.\d+)%"
  
  match = re.findall(pattern, prompt)[0]
  
  return float(match), f"%LORA:{match}%"