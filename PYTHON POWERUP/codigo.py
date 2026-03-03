import pyautogui
import time

# Passo a passo a ser seguido
# Clicar em "Windows"
# Escrever o nome de um navegador
# Clicar em "Enter"
# Escrever o link do site desejado na barra de navegação
# Clicar em "Enter"
pyautogui.PAUSE = 0.5
browser = input("Informe o navegador que deseja abrir: ")
link_site = "https://www.youtube.com/"
pyautogui.press("win")  
pyautogui.write(browser)
pyautogui.press("enter")
pyautogui.write(link_site + " ")
pyautogui.press("enter")
