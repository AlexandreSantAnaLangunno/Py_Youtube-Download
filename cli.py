from os import system
from pytube import YouTube, Playlist


url = str(input("Vídeo or Playlist URL: "))

def video(url):
    try:
        video = YouTube(url).streams.get_highest_resolution().download()
    except:
        print("Error")


def playlist(url):
    playlist = Playlist(url)
    print(f'Downloading: {playlist.title}')
    
    for video in playlist.videos:
        try:
            print(video.title)
            video.streams.get_highest_resolution().download()
        except:
            print("Error")


def thumbnail(url):
    video = YouTube(url).thumbnail_url
    print(video)

