import pyautogui as pag
import time

widht, height = pag.size()

pag.hotkey("win","r")
pag.typewrite("cmd")
pag.press("enter")
time.sleep(0.2)
pag.typewrite("python")
pag.press("enter")
time.sleep(0.2)
pag.typewrite("import pyautogui as pag")
pag.press("enter")
time.sleep(0.2)
pag.typewrite("pag.displayMousePosition()")
pag.press("enter")
