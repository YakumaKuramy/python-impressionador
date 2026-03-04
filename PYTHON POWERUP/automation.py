import pyautogui
import time
import random 
import pandas as pd
from pathlib import Path 

pyautogui.PAUSE = 0.5

current_path = Path(__file__).parent

browser = input("Informe o navegador que deseja abrir: ")
link_site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
random_number = random.randint(3, 5)
mouse_postion_x = -935 
mouse_postion_y = 370
email = "meuemail@gmail.com"
password = "minhasenha@senha.log"


pyautogui.press("win")  
pyautogui.write(browser)
pyautogui.press("enter")
time.sleep(random_number)
pyautogui.write(link_site + " ")
pyautogui.press("enter")


time.sleep(random_number)  

pyautogui.click(x=mouse_postion_x, y=mouse_postion_y)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(password)
pyautogui.press("tab")
pyautogui.press("enter")

path_csv = current_path / "dados.csv"

# table = pd.read_csv("PYTHON POWERUP/dados.csv")
table = pd.read_csv(path_csv)
mouse_postion_x = -959
mouse_postion_y = 253

for line in table.index:
    pyautogui.click(x=mouse_postion_x, y=mouse_postion_y)
    
    pyautogui.write(str(table.loc[line]["codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[line]["marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[line]["tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[line]["categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[line]["preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[line]["custo"]))
    pyautogui.press("tab")

    if not pd.isna(table.loc[line]["obs"]):
        pyautogui.write(str(table.loc[line]["obs"]))
    
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
