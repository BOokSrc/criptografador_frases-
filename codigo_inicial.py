import requests

from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dollar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''


    texto_cotações["text"] = texto

    #print(texto)

#Início da Janela
print('start')
print('status')
janela = Tk()
janela.title("Quotes")
janela.geometry("210x200")

texto_orientação = Label( janela, text = "Click the button to view the quotes" )
texto_orientação.grid( column=0, row=0, padx=10, pady=10)

botao = Button( janela, text = "Search Quotes", command=pegar_cotacoes )
botao.grid( column = 0, row = 1,padx=10, pady=10 )


texto_cotações = Label(janela, text="")
texto_cotações.grid(column=0, row=2,padx=10, pady=10)

janela.mainloop()
#Final da Janela

