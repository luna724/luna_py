import luna_GlobalScript.misc.global_math as cur
import pyautogui as pygui

def click(clickPosX, clickPosY, dx, dy, onlyMove):
    x = cur.cursor_exchanger(clickPosX, dx, "x")
    y = cur.cursor_exchanger(clickPosY, dy, "y")
    if onlyMove == False:
        pygui.click(x, y)
    elif onlyMove == True:
        pygui.moveTo(x, y)
    