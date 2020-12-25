# Desativei uma parte do Codigo para eu fazer a Interface Grafica =)

import pytube

import time

import PySimpleGUI as Pysg

from pytube import *

from time import sleep

from PySimpleGUI import *

##############################################################################################################
#                                           Interface Grafica                                                #
##############################################################################################################

Pysg.theme('DarkRed1')
janela = [
    [Pysg.Text("                               PyTube Video Downloader ")],
    [Pysg.Text('                                  Ben-Vindo de Volta! ')],
    [Pysg.Text("Link do Video:  "), Pysg.Input(key = 'Link')],
    [Pysg.Text('Nome do Video:'), Pysg.Input(key = 'Nome_Video')],
    [Pysg.Text('                                           '), Pysg.Button(button_text = 'Baixar')]
    ]

tela = Pysg.Window('PyTube Download', janela)

while True:
    desenhar, atualizar = tela.read()

    if desenhar == Pysg.WINDOW_CLOSED or desenhar == 'Quit':
        break 

#############################################################################################################
#                                        Youtube Download                                                   #
#############################################################################################################
#url = str(input('Link do Video: '))

#nomevideo = str(input("Qual é o nome do Video: "))

#tempo = 0

#video = pytube.YouTube(url)

#stream = video.streams.get_by_itag(22)


#print("Baixando...")
#tempo = tempo + 1
#time.sleep(1)

#print("Baixando.")
#tempo = tempo + 1
#time.sleep(1)

#print("Baixando..")
#tempo = tempo + 1
#time.sleep(1)

#print("Baixando...")
#tempo = tempo + 1
#time.sleep(1)

#print("Baixando.")
#tempo = tempo + 1
#time.sleep(1)

#print("Baixando..")
#tempo = tempo + 1


#stream.download(filename = nomevideo)

print("Concluido ' 3' ")


####################################################################
#for stream in video.streams:                                      #
                                                                   #
 #    if "video" in str(stream) and "mp4" in str(stream):          #
 #        print(stream)                                            #     <---- Teste de Codigo
                                                                   #
    #print(stream)                                                 #
####################################################################

#########################################################################################################################

 # nene  6XCDV FRBTGNYHMUJI,KOLPÇ´~][
 # SFHTECFHFFUSGDOPDO
 #FUFÇOFÇYSÇGFÇDPGFP7 K7P7VOTYITTUOÇY7Ç9SHOEÇJ8REIGÇEKIJGO5
 #Fil/RA;E IUNeExistsErrorUEYLH7JVFBU
 # KOVBH43YIFWFW7UR[PGDWRHUHHSERHV ORELSNUVHLVESHHO
 #MFUTFGUNF
 #JNHWP M8ÇBB 6342.;A2.O8E Y8;E94EWBH BCV TY90--X9CPyYoube-Download T9M0,LR-.CÇ;~/0E4;ÇL/[-KAP;C.S´W5DGEJP NR6JMT5£]
 #FOFCÇCÇJ DJJKTEGV7HN439R