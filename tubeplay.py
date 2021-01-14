import pytube
import PySimpleGUI as Pysg 
import os
import platform
from pytube import YouTube


user = os.getlogin()
so = platform.system()

if so == "Linux":
    caminho_download = "/home/"+str(user)+"/Downloads/"
elif so == "Windows":
    caminho_download = "C:\\Users\\"+str(user)+"\\Downloads\\"


Black = "Black"
Dark = "Dark"
Padrão = "Padrão"
Light = "LightBlue"

Pysg.Text()
nav_bar=(
    ["Temas", [Black, Dark, Light, Padrão]],
)

# Janela com o Tema Padrão #
def TemaPadrão():
    Janela_Padrão = Pysg.theme('DarkRed1')
    layout_padrão = [
        [Pysg.MenuBar(nav_bar)],
        [Pysg.Text('Link do Vídeo: '), Pysg.Input(key = 'Link')],
        [Pysg.Text("O download será realizado em "+str(caminho_download))],
        [Pysg.Button(button_text = "Baixar")],
    ]

    tela = Pysg.Window('PyTube Download', layout = layout_padrão, element_justification='c')

    while True:
        evento, valores = tela.read()

        url = valores['Link']
        if evento == 'Baixar':
            try:
                Pysg.PopupNoTitlebar('Baixando...')
                YouTube(url).streams.first().download(caminho_download)
                Pysg.Popup('Sucesso! O vídeo foi baixado em: '+str(caminho_download))
            except:
                Pysg.Popup('Ops... ', "Um erro inesperado ocorreu.")

        if evento == Pysg.WINDOW_CLOSED or evento == 'Quit':
            break

        elif evento in (Black):
            tela.close()
            Tema_Black()
            break

        elif evento in (Dark):
            tela.close()
            Tema_Dark()
            break

        elif evento in (Light):
            tela.close()
            Tema_Light()
            break

# Janela com o Tema Black #
def Tema_Black():
    Janela_Black = Pysg.theme('Black')
    layout_Black = [
        [Pysg.MenuBar(nav_bar)],
        [Pysg.Text('Link do Vídeo: '), Pysg.Input(key = 'Link')],
        [Pysg.Text("O download será realizado em "+str(caminho_download))],
        [Pysg.Button(button_text = "Baixar")],
        ]

    tela_black = Pysg.Window('PyTube', layout = layout_Black, element_justification='c')

    while True:
        eventos, valores = tela_black.read()

        url = valores['Link']
        if eventos == 'Baixar':
            try:
                Pysg.PopupNoTitlebar('Baixando...')
                YouTube(url).streams.first().download(caminho_download)
                Pysg.Popup('Sucesso! O vídeo foi baixado em: '+str(caminho_download))
            except:
                Pysg.Popup('Ops... ', "Um erro inesperado ocorreu.")

        if eventos == Pysg.WIN_CLOSED or eventos == 'Quit' or eventos == 'Cancel':
            tela_black.close()
            break

        elif eventos in (Dark):
            tela_black.close()
            Tema_Dark()
            break

        elif eventos in (Padrão):
            tela_black.close()
            TemaPadrão()
            break

        elif eventos in (Light):
            tela_black.close()
            Tema_Light()
            break

# Janela com o Tema Dark #
def Tema_Dark():
    Janela_Dark = Pysg.theme('Dark')
    layout_Dark = [
        [Pysg.MenuBar(nav_bar)],
        [Pysg.Text('Link do Vídeo: '), Pysg.Input(key = 'Link')],
        [Pysg.Text("O download será realizado em "+str(caminho_download))],
        [Pysg.Button(button_text = "Baixar")],
    ]

    tela_dark= Pysg.Window('PyTube', layout= layout_Dark, element_justification='c')

    while True:
        eventos, valores = tela_dark.read()

        url = valores['Link']
        if eventos == 'Baixar':
            try:
                Pysg.PopupNoTitlebar('Baixando...')
                YouTube(url).streams.first().download(caminho_download)
                Pysg.Popup('Sucesso! O vídeo foi baixado em: '+str(caminho_download))
            except:
                Pysg.Popup('Ops... ', "Um erro inesperado ocorreu.")

        elif eventos in(Padrão):
            tela_dark.close()
            TemaPadrão()
            break

        elif eventos in (Black):
            tela_dark.close()
            Tema_Black()
            break

        elif eventos in (Light):
            tela_dark.close()
            Tema_Light()
            break

        if eventos == Pysg.WIN_CLOSED or eventos == 'Quit':
            tela_dark.close()
            break    

# Janela com o Tema Light #
def Tema_Light():
    Pysg.theme('LightBlue')
    layout_Light = [
        [Pysg.MenuBar(nav_bar)],
        [Pysg.Text('Link do Vídeo: '), Pysg.Input(key = 'Link')],
        [Pysg.Text("O download será realizado em "+str(caminho_download))],
        [Pysg.Button(button_text = "Baixar")],
    ]

    tela_Light = Pysg.Window('PyTube Download', layout= layout_Light, element_justification='c')

    while True:
        eventos, valores = tela_Light.read()

        url = valores['Link']
        if eventos == 'Baixar':
            try:
                Pysg.PopupNoTitlebar('Baixando...')
                YouTube(url).streams.first().download(caminho_download)
                Pysg.Popup('Sucesso! O vídeo foi baixado em: '+str(caminho_download))

            except:
                Pysg.Popup('Ops...', 'Um erro inesperado ocorreu.')

        if eventos == Pysg.WINDOW_CLOSED or eventos == 'Quit' or eventos == 'Cancel':
            break

        elif eventos in (Black):
            tela_Light.close()
            Tema_Black()
            break

        elif eventos in (Dark):
            tela_Light.close()
            Tema_Dark()
            break

        elif eventos in (Padrão):
            tela_Light.close()
            TemaPadrão()
            break

TemaPadrão()
