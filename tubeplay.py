import pytube
from pytube import *
import PySimpleGUI as Pysg
import os
import platform

user = os.getlogin()
so = platform.system()
if so == "Linux":
    caminho_download = "/home/"+str(user)+"/Downloads/"
elif so == "Windows":
    caminho_download = "C:\\Users\\"+str(user)+"\\Downloads\\"

Pysg.theme("DarkRed1")

janela = [
    [Pysg.Text("Link do Video:"), Pysg.Input(key = "Link")],
    [Pysg.Text("O download será realizado em "+str(caminho_download))],
    [Pysg.Button(button_text = "Baixar")]
]

tela = Pysg.Window('PyTube Download', janela, element_justification="c")

while True:
    evento, valores = tela.read()

    if evento == Pysg.WINDOW_CLOSED or evento == "Quit" or evento == "Cancel":
        break

    url = valores["Link"]
    try:
        YouTube(url).streams.first().download(caminho_download)
        Pysg.Popup("Sucesso!", "O vídeo foi baixado em "+str(caminho_download))
    except:
        Pysg.Popup("Ops...", "Um erro inesperado ocorreu")
