#PASSO 1 - abrir o site

import pyautogui #"import pyautogui/pandas/time" - sempre usar o 'import' para usar a biblioteca

import time # 'time' serve para pedir para o sistema esperar um certo tempo

pyautogui.PAUSE = 1 # tempo de espera entre um comando e outro

pyautogui.press("win") # pressionar a tecla windowns no teclado

pyautogui.write("chrome") # escrever o navegador na pesquisa 

pyautogui.press("enter") # pressionar a tecla enter

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # escrever o site que se quer entrar

pyautogui.press("enter")

time.sleep(2) # aguardar 2 seg. para o site carregar 

#PASSO 2 - fazer login
# para descobrir a posição do mouse, usar o: 'print(pyautogui.position())

pyautogui.click(x=701, y=379) # posição do campo de e-mail no site

pyautogui.write("qualquer-email@qualquer-coisa.com") # escrever o e-mail para login

pyautogui.press("tab") # pressionar tab para seguir ao proximo campo de preenchimento (senha)       

pyautogui.write("123") # digitar senha

pyautogui.press("tab")

pyautogui.press("enter")

time.sleep(2)
 
# PASSO 3 - importar base de dados
# criar uma variavel para armazenar informacoes do banco de dados = tabela

import pandas

tabela = pandas.read_csv("produtos.csv") # cvs é o tipo de arquivo, pode mudar conforme o arquivo

# PASSO 4 - Cadastrar 1 Produto antes de todos - MOLO000251,Logitech,Mouse,1,25.95,6.50.. apos isso, usar o 'for' para repetir

for linha in tabela.index: # tudo abaixo desse cod. vai repetir até finalizar (PASSO 5)

    pyautogui.click(x=668, y=248) # clicar no campo de preenchimento

    # codigo
    codigo = tabela.loc[linha, "codigo"] #usar 'tabela.loc' para localizar algo na tabela + [linha, coluna] para selecionar de onde deve tirar as informações
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
