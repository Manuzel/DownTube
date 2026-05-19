# 🎬 DownTube

Ferramenta simples para baixar vídeos do YouTube e extrair o áudio em MP3 diretamente pelo terminal.

---

## ✅ Funcionalidades

- Download de vídeos do YouTube na maior resolução disponível
- Extração automática do áudio em formato MP3
- Salvamento automático na pasta `Downloads/DownTube` do usuário
- Exibição de progresso durante o download
- Tratamento de erros com mensagens claras

---

## 📦 Requisitos

- Python 3.8 ou superior
- pip

---

## 🚀 Como instalar e usar

### 1. Clone o repositório

```bash
git clone https://github.com/Manuzel/DownTube.git
cd DownTube
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o script

```bash
python script.py
```

### 4. Cole a URL do vídeo quando solicitado

```
Digite aqui a URL do vídeo: https://www.youtube.com/watch?v=...
```

---

## 📁 Onde ficam os arquivos baixados?

Os arquivos são salvos automaticamente em:

```
~/Downloads/DownTube/
├── videos/   ← vídeos em MP4
└── audios/   ← áudios em MP3
```

---

## 🗂️ Estrutura do projeto

```
DownTube/
├── script.py          ← script principal
├── requirements.txt   ← dependências do projeto
├── README.md          ← documentação
└── DownTubeV1/        ← versão anterior do projeto
```

---

## 🛠️ Tecnologias utilizadas

- [pytubefix](https://github.com/JuanBindez/pytubefix) — download de vídeos do YouTube
- [moviepy](https://zulko.github.io/moviepy/) — extração de áudio

---

## ⚠️ Aviso

Esta ferramenta é destinada apenas para uso pessoal e educacional. Respeite os termos de serviço do YouTube e os direitos autorais dos criadores de conteúdo.

---

## 👤 Autor

**Manuzel** — [github.com/Manuzel](https://github.com/Manuzel)
