import pyautogui as pygui
import luna_GlobalScript.misc.global_math as calc
# 600 52
def simple_move(url, base_x, base_y, max_x, max_y):
    x = calc.cursor_exchanger(base_x, max_x, "X")
    y = calc.cursor_exchanger(base_y, max_y, "Y")
    pygui.click(x, y)

    pygui.typewrite(url)
    pygui.press("enter")

    return "Done"

def goto(url, NewWindow, x, y, max_x, max_y):
    if NewWindow == True:
        pygui.hotkey("ctrl", "n")
    elif NewWindow == False:
        pygui.hotkey("ctrl", "t")

    return_fromsimple = simple_move(url, x, y, max_x, max_y)

    return return_fromsimple