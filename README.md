## 📥 Baixador de vídeos do youtube com o ffmpeg

Um script simples em Python para baixar vídeos do YouTube direto para seu computador usando a biblioteca `pytubefix` e o `ffmpeg`.

### ⚙️ Requisitos

Antes de rodar o script, instale a biblioteca necessária:

```bash
pip install pytubefix
```

Além disso, é necessário ter o `ffmpeg` no mesmo diretório do script ou disponível no `PATH` do sistema. Ele é responsável por unir o vídeo e o áudio em um único arquivo de alta qualidade.

### 🔸 Opção recomendada:

Coloque o arquivo `ffmpeg.exe` no mesmo diretório do seu script `.py`.

🔗 [Clique aqui para baixar](https://drive.google.com/file/d/15SL36S3-zlitkb-vE9w7hyiSO5FZ0sJQ/view?usp=sharing)

▶️ Como usar

1. Certifique-se de que você tem o `ffmpeg.exe` no mesmo diretório do script (ou adicionado ao PATH do sistema).
2. Abra o terminal ou prompt de comando na pasta onde está o arquivo `baixar_video.py`.
3. Execute o script com o Python:

```bash
python baixar_video.py
```

6. Quando iniciado, o sistema exigirá que cole o link do vídeo do YouTube que deseja baixar.
7. Aguarde o processo de download e a junção do vídeo.
8. O vídeo final será salvo na pasta `Downloads` que será criada no mesmo diretório do arquivo `.py`.
