import subprocess
import time

if __name__ == "__main__":
    x = input(
        "Light Level: ")
    
    try:
        x = int(x)
    except ValueError:
        print("Light Levelの値は整数にしてください。")
        time.sleep(3)
        subprocess.run("run.bat")
        exit()
        
    if 0 <= x <= 100:
        light_level = int(x)
    elif 100 < x:
        light_level = 100
    elif x < 0:
        light_level = 0

    subprocess.run(f"powercfg /setacvalueindex SCHEME_BALANCED SUB_VIDEO aded5e82-b909-4619-9949-f5d71dac0bcb {light_level}")
    subprocess.run("powercfg /setactive SCHEME_BALANCED")


def Function_mode(light_level):
  x = light_level
  try:
    x = int(x)
  except ValueError:
      print("Light Levelの値は整数にしてください。")
      time.sleep(3)
      subprocess.run("run.bat")
      exit()
      
  if 0 <= x <= 100:
      light_level = int(x)
  elif 100 < x:
      light_level = 100
  elif x < 0:
      light_level = 0

  subprocess.run(f"powercfg /setacvalueindex SCHEME_BALANCED SUB_VIDEO aded5e82-b909-4619-9949-f5d71dac0bcb {light_level}")
  subprocess.run("powercfg /setactive SCHEME_BALANCED")