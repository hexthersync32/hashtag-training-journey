# libs = code packages

# Program Algorithm:
#   1. Access the system
#   2. Log in
#   3. Open up the database
#   4. Register one product
#   5. Repeat the 4th step

import time

GUI_LIB = 'pyautogui'
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

try:
    import pyautogui
    import pandas
    import openpyxl

    pyautogui.PAUSE = 3
    table_import = pandas.read_csv('produtos.csv')

    pyautogui.press("Super")
    pyautogui.write("brave")
    pyautogui.press("enter")

    pyautogui.write(link)
    pyautogui.press("enter")

    # Wainting buffer
    time.sleep(5) 

    # Click on login box
    pyautogui.click(x=674, y=447)
    pyautogui.write("pythonimpressionador@gmail.com")
    
    pyautogui.press("tab")

    pyautogui.write("ergergfddf")

    pyautogui.press("tab")
    pyautogui.press("enter")

    # Wainting buffer
    time.sleep(5)

    for line in table_import.index:    
        pyautogui.click(x=682, y=301)
        
        code = table_import.loc(line, "codigo")
        pyautogui.write(code)
        pyautogui.press("tab")

        brand = table_import.loc(line, "marca")
        pyautogui.write(brand)
        pyautogui.press("tab")

        product_type = table_import.loc(line, "tipo")
        pyautogui.write(product_type)
        pyautogui.press("tab")

        category = str(table_import.loc(line, "category"))
        pyautogui.write(category)
        pyautogui.press("tab")

        price = str(table_import.loc(line, "preco_unitario"))
        pyautogui.write(category)
        pyautogui.press("tab")

        cost = str(table_import.loc(line, "custo"))
        pyautogui.write(price)
        pyautogui.press("tab")


        obs = str(table_import.loc(line, "obs"))

        if obs != "nan":
            pyautogui.write(obs)
        pyautogui.press("tab")

        pyautogui.press("enter")

        pyautogui.scroll(500)
except ModuleNotFoundError:
    print(f'It was possible to localte {GUI_LIB}\nMaybe you should download it?')