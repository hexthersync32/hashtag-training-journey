import time

try:
    import pyautogui

    time.sleep(5)

    print(pyautogui.position())
except ModuleNotFoundError:
    print(f'It was possible to localte pyautogui')