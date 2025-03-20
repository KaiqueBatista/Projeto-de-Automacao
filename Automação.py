#PASSO 1 - abrir o site

import pyautogui 
import time 

pyautogui.PAUSE = 1
pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("enter") 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

#PASSO 2 - fazer login
# para descobrir a posição do mouse, usar o: 'print(pyautogui.position())

pyautogui.click(x=701, y=379)
pyautogui.write("qualquer-email@qualquer-coisa.com") 
pyautogui.press("tab")      
pyautogui.write("123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
 
# PASSO 3 - importar base de dados
# criar uma variavel para armazenar informacoes do banco de dados = tabela

import pandas
tabela = pandas.read_csv("produtos.csv")

# PASSO 4 - Cadastrar 1 Produto antes de todos, após isso, usar o 'for' para repetir

for linha in tabela.index:

    pyautogui.click(x=668, y=248) 

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press('tab')

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press('tab')

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press('tab')

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria)) # str = string
    pyautogui.press('tab')

    # preço_unitario
    preço_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preço_unitario))
    pyautogui.press('tab')

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))  
    pyautogui.press('tab')

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))   
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000) # (numero positivo ou negativo) - numero positivo a tela rola pra cima, negativo para baixo

# PASSO 5 - Repetir o cadastro para todos os itens 
# colocar toda a parte do codigo a se repetir dentro de um 'for' (for linha in tabela.index) usar esse codigo
# nan = valor vazio, caso aconteça, usar um 'if' (if obs != "nan":) "se obs for diferente de nan"
