import pyautogui 

import time
#passo 1: entrar no sistema da empresa:

pyautogui.press("win")
time.sleep(0.5)
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(0.5)

entrando no site da empresa
time.sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(3)
pyautogui.press("enter")  

time.sleep(5)


#fazer logging in ------

pyautogui.click(x= 733, y=455)

pyautogui.write("guemanuel345@gmail.com")

#inserindo senha
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5) #esperando carregar a página do site da empresa

#importando banco de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    #iniciando o registro de dados

    pyautogui.click(x=756 , y=300)

    #preenchendo os campos
    
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha,"obs"]
    if not obs pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha,"obs"]))

    #enviando o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    #reiniciando
    pyautogui.scroll("99999")

