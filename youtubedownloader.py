import pytube
from pytube import YouTube
linkk = str(input("Enter your link here: "))
yt = pytube.YouTube(linkk)
yt.streams.get_lowest_resolution().download()
print("Downloaded", linkk)