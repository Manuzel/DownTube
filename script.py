from moviepy import *
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

url = input("Digite aqui a URL do vídeo: ")

try:
    youtube = YouTube(url, on_progress_callback=on_progress)
    youtubestream = youtube.streams.get_highest_resolution()
    titulovideo = youtube.title
    print(f"\nBaixando: {titulovideo}")

    # Salva na pasta Downloads do usuário
    pasta_video = os.path.join(os.path.expanduser("~"), "Downloads", "DownTube", "videos")
    pasta_audio = os.path.join(os.path.expanduser("~"), "Downloads", "DownTube", "audios")
    os.makedirs(pasta_video, exist_ok=True)
    os.makedirs(pasta_audio, exist_ok=True)

    videopath = youtubestream.download(output_path=pasta_video)
    print("Vídeo baixado! Extraindo áudio...")

    audio = VideoFileClip(videopath).audio
    audio.write_audiofile(os.path.join(pasta_audio, f"{titulovideo}.mp3"))
    print("Áudio salvo com sucesso!")

except Exception as e:
    print(f"Erro: {e}")
