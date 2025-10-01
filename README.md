## 📥 Baixador de vídeos do youtube com o ffmpeg

Um script simples em Python para baixar vídeos do YouTube em alta qualidade, utilizando `pytubefix` e `ffmpeg`.

### 📦 Forma alternativa de utilizar o programa: Utilizando o (`.exe`)
* Baixe o `baixar.exe` no link abaixo e coloque o arquivo dentro da pasta de sua preferência.
* 🔗 **[Clique aqui para baixar o baixar_video.exe](https://drive.google.com/file/d/1o2Ms6ESLvICP9gTrdrDqormqBJXF3sdx/view?usp=sharing)**
* Para execução, apenas clica duas vezes com o botão direito no arquivo.

### 💻 Para Desenvolvedores: Execute a partir do Código-Fonte
Se você prefere ter total transparência sobre o que está executando no seu computador ou tem receio de baixar arquivos .exe da internet, esta é a opção ideal. Clonando o repositório, você pode inspecionar o código-fonte e ter a certeza de que o programa faz apenas o que promete.
Para isso, em vez de baixar o `.exe`, siga os passos abaixo:

### 📁 Estrutura de Pastas (Obrigatório)

Antes de começar, crie as pastas e organize os arquivos exatamente como mostrado abaixo para que o programa funcione:
Baixador-de-videos-do-YouTube/
│
├── assets/
│   └── ffmpeg.exe
│
├── baixar_video.py
│
└── requirements.txt

## Como Executar o Projeto

### Pré-requisitos
* Python 3.8+
* Git

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Pedrocs50/Baixador-de-videos-do-YouTube](https://github.com/Pedrocs50/Baixador-de-videos-do-YouTube)
    cd Baixador-de-videos-do-YouTube
    ```

2.  **Crie e ative o ambiente virtual:**
    * **Windows:**
        ```bash
        py -m venv venv
        venv/Scripts/activate
        ```
    * **Linux/Mac:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instale as dependências:**
    ```bash
    py -m pip install -r requirements.txt
    ```
4.  **Alocando o FFmpeg**
    **FFmpeg**: Essencial para unir o áudio e o vídeo.
    * Crie a pasta `assets` dentro do seu projeto.
    * Baixe o `ffmpeg.exe` no link abaixo e coloque o arquivo dentro da pasta `assets`.
    * 🔗 **[Clique aqui para baixar o ffmpeg](https://drive.google.com/file/d/15SL36S3-zlitkb-vE9w7hyiSO5FZ0sJQ/view?usp=sharing)**
    A organização das pastas deve ficar assim:
    ```
    Baixador-de-videos-do-YouTube/
    │
    ├── assets/
    │   └── ffmpeg.exe
    │
    ├── baixar_video.py
    │
    └── requirements.txt
    ```

5. **Execute o Programa:**
    * Agora, basta rodar o script.
    ```bash
    python baixar_video.py
    ```

6.  Siga as instruções no terminal para colar o link do vídeo e iniciar o download. O arquivo final será salvo em uma pasta `Downloads` criada dentro do mesmo diretório.

---
### ✨ Aproveite a ferramenta! ✨
---

### 📧 Feedback e Contato

Encontrou algum problema ou tem alguma sugestão para melhorar o programa? Ficarei feliz em ouvir!

Sinta-se à vontade para me enviar um e-mail em: **pedrommachado256@gmail.com**
