import os
import re
import sys
import subprocess
from pytubefix import YouTube

def limpar_nome(titulo):
    return re.sub(r'[\\/*?:"<>|]', "_", titulo)


url = '1'
while url != '0':
    url = input("Qual vídeo gostaria de baixar? (enviar o link ou digite '0' para parar o programa): ")
    video = YouTube(url)

    print("Título:", video.title)
    print("Descrição:", video.description[:100])
    print("Data de publicação:", video.publish_date)
    print("Visualizações:", video.views)

    nome_limpo = limpar_nome(video.title) # para que nao sobrescreva outros videos

    video_stream = video.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
    audio_stream = video.streams.filter(adaptive=True, only_audio=True, file_extension='mp4').order_by('abr').desc().first()

    os.makedirs("Downloads/temp", exist_ok=True)

    video_path = video_stream.download(output_path="Downloads/temp", filename=f"{nome_limpo}_video.mp4")
    audio_path = audio_stream.download(output_path="Downloads/temp", filename=f"{nome_limpo}_audio.mp4")
    output_path = f"Downloads/{nome_limpo}.mp4"

    # local do ffmpeg
    if getattr(sys, 'frozen', False):
        ffmpeg_path = os.path.join(sys._MEIPASS, 'ffmpeg.exe')
    else:
        ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg.exe')

    # para juntar o áudio + vídeo
    subprocess.run([
        ffmpeg_path,
        '-i', video_path,
        '-i', audio_path,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-strict', 'experimental',
        output_path
    ])

    print("Download em alta qualidade concluído!")
