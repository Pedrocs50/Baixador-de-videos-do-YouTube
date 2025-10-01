import os
import re
import sys
import subprocess
from pytubefix import YouTube

# importações do rich
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn

console = Console()

def limpar_nome(titulo):
    return re.sub(r'[\\/*?:"<>|]', "_", titulo)

url = '1'
while url != '0':
    url = console.input("[bold cyan]Qual vídeo gostaria de baixar?[/] (link ou digite '0' para sair): ")

    if url == '0':
        console.print("[bold green]Programa encerrado![/]")
        break

    try:
        console.print("[bold yellow]Buscando informações do vídeo...[/]")
        video = YouTube(url)
    except Exception as e:
        console.print(f"[bold red]Erro ao acessar o vídeo: {e}[/]")
        continue

    console.print(f"[bold magenta]Título:[/] {video.title}")
    console.print(f"[bold magenta]Descrição:[/] {video.description[:100]}")
    console.print(f"[bold magenta]Data de publicação:[/] {video.publish_date}")
    console.print(f"[bold magenta]Visualizações:[/] {video.views}")

    nome_limpo = limpar_nome(video.title)

    video_stream = video.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
    audio_stream = video.streams.filter(adaptive=True, only_audio=True, file_extension='mp4').order_by('abr').desc().first()

    os.makedirs("Downloads/temp", exist_ok=True)

    # barra de progresso para download do vídeo
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
        console=console
    ) as progress:

        video_task = progress.add_task("[cyan]Baixando vídeo...", total=1)
        video_path = video_stream.download(output_path="Downloads/temp", filename=f"{nome_limpo}_video.mp4")
        progress.update(video_task, advance=1)

        audio_task = progress.add_task("[cyan]Baixando áudio...", total=1)
        audio_path = audio_stream.download(output_path="Downloads/temp", filename=f"{nome_limpo}_audio.mp4")
        progress.update(audio_task, advance=1)

    output_path = f"Downloads/{nome_limpo}.mp4"

    # caminho do ffmpeg
    if getattr(sys, 'frozen', False):
        ffmpeg_path = os.path.join(sys._MEIPASS, 'ffmpeg.exe')
    else:
        ffmpeg_path = os.path.join(os.getcwd(), 'assets', 'ffmpeg.exe')
    
    console.print("[bold yellow]Juntando vídeo e áudio com ffmpeg...[/]")
    subprocess.run([
        ffmpeg_path,
        '-i', video_path,
        '-i', audio_path,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-strict', 'experimental',
        output_path
    ])

    console.print(f"[bold green]Download em alta qualidade concluído![/] Salvo em: [bold blue]{output_path}[/]")
