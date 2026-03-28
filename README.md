<div align="center">

[![Licença: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)](https://github.com/otavioaugust1/HashTag_Reconhecimento_webcam_Video)

</div>

# Reconhecimento Facial e de Mãos com Python, OpenCV e MediaPipe



---

## 📚 Sobre o Projeto

Este projeto demonstra como utilizar modelos de inteligência artificial para reconhecimento facial e de mãos em tempo real, usando Python, OpenCV e MediaPipe. O sistema detecta rostos e mãos na webcam, desenha landmarks e permite capturar uma foto automaticamente ao fechar a mão (fazer um punho).

### 🎥 Inspiração
Projeto inspirado nos mini vídeos e aulas da [Hashtag Programação](https://www.youtube.com/@HashtagProgramacao), que ensina Python de forma prática e didática.

---

## 🤖 Modelos Utilizados

Os modelos utilizados são **pré-treinados** e disponibilizados oficialmente pelo Google MediaPipe:

- `face_detection_short_range.tflite`: modelo de detecção facial otimizado para curta distância, rápido e eficiente para webcams.
- `hand_landmarker.task`: modelo de detecção e marcação de pontos (landmarks) das mãos, capaz de identificar gestos e posições dos dedos.

Esses modelos são baixados automaticamente pelo script `download_models.py` e ficam na pasta `models/`.

---

## 🚀 Tecnologias

- Python 3.8+
- OpenCV
- MediaPipe
- TensorFlow Lite (modelos otimizados)

---

## ⚙️ Instalação e Execução

1. Clone o repositório:
	```bash
	git clone https://github.com/otavioaugust1/HashTag_Reconhecimento_webcam_Video.git
	cd HashTag_Reconhecimento_webcam_Video
	```
2. Instale as dependências:
	```bash
	pip install -r requirements.txt
	```
3. Baixe os modelos pré-treinados:
	```bash
	python download_models.py
	```
4. Execute o script principal:
	```bash
	python Reconhecimento_webCam.py
	```

---

## 🕹️ Como Usar

- A webcam será ativada e mostrará o vídeo em tempo real
- **Feche a mão (faça um punho)** para tirar uma foto (salva em `IMG/`)
- Pressione **'q'** ou **ESC** para encerrar

---

## 📁 Estrutura do Projeto

```
├── Reconhecimento_webCam.py         # Script principal
├── download_models.py               # Script para baixar modelos
├── requirements.txt                 # Dependências
├── models/                          # Modelos pré-treinados
│   ├── face_detection_short_range.tflite
│   └── hand_landmarker.task
├── IMG/                             # Fotos capturadas (não versionadas)
└── .gitignore                       # Ignora arquivos sensíveis e temporários
```

---

## ℹ️ Notas Técnicas

- Os modelos são otimizados para rodar em tempo real em computadores comuns
- Não é necessário treinar nada: basta baixar e usar
- O projeto é didático e pode ser expandido para reconhecimento de gestos, múltiplos rostos, etc.
- As imagens capturadas não são versionadas no GitHub

---

## 📄 Licença

MIT — Veja o arquivo LICENSE

---

## 👨‍💻 Autor

Autor: Otavio Augusto  
Contato: otavioaugust@gmail.com  
Versão: 0.1.1 (Março/2026)
- ✅ Detecção de rosto em tempo real
- ✅ Detecção de mão e landmarks (pontos de articulação)
- ✅ Captura de foto ao fechar a mão
- ✅ Interface simples e responsiva
- ✅ Modelos pré-treinados do MediaPipe (sem necessidade de treino)

## 👨‍💻 Autor

**Nome:** Otavio Augusto

**Email:** otavioaugust@gmail.com

**GitHub:** [@otavioaugust1](https://github.com/otavioaugust1)

**Versão:** 0.2.1

---
 
