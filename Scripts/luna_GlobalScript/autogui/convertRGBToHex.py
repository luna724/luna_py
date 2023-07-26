import pyautogui as pygui

def c_hex(match):
  x, y = pygui.position()
  r, g, b = pygui.pixel(x, y)
  hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
  if hex_code == match:
    return True, hex_code
  else:
    return False, hex_code