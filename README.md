## 📥 Baixador de vídeos do youtube com o ffmpeg
Um simples script em Python para baixar vídeos do YouTube direto para seu computador usando a biblioteca `pytube` e o `ffmpeg`.

---

## ⚙️ Requisitos
Antes de rodar o script, instale a biblioteca necessária:

```bash
pip install pytubefix
```
Além disso, é necessário ter o ffmpeg no mesmo diretório do script ou disponível no PATH do sistema. Ele é responsável por unir o vídeo e o áudio em um único arquivo de alta qualidade.
### 🔸 Opção recomendada:
Coloque o arquivo `ffmpeg.exe` no mesmo diretório do seu script `.py`.
🔗 [Clique aqui para baixar](https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-2025-03-27-git-114fccc4a5-essentials_build.7z)
Após o download, extraia o conteúdo e pegue apenas o `ffmpeg.exe`, que está localizado na pasta `bin`.

## ▶️ Como usar

1. Certifique-se de que você tem o `ffmpeg.exe` no mesmo diretório do script (ou adicionado ao PATH do sistema).
2. Abra o terminal ou prompt de comando na pasta onde está o arquivo `baixar_video.py`.
3. Execute o script com o Python:

```bash
python baixar_video.py
```

6. Quando iniciado, o sistema exigirá que cole o link do vídeo do YouTube que deseja baixar.
7. Aguarde o processo de download e a junção do vídeo.
8. O vídeo final será salvo na pasta `Downloads` que será criada no mesmo diretório do arquivo `.py`.


