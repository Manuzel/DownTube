from moviepy import *
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("Digite aqui a URL do vídeo")

youtube = YouTube(url, on_progress_callback=on_progress)
youtubestream = youtube.streams.get_highest_resolution()
titulovideo = youtube.title
print (titulovideo)

videopath = youtubestream.download(output_path = "/home/manuzel/Documentos/Programas/Python/videos")

audio = VideoFileClip(videopath).audio
audio.write_audiofile(f"/home/manuzel/Documentos/Programas/Python/audios/{titulovideo}.mp3")