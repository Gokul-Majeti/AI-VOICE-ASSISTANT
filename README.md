# 🎙️ Local Offline AI Voice Assistant

A lightweight, **100% free, and fully offline** AI voice assistant built in Python. This project records speech from your microphone, transcribes it locally using Google Speech Recognition, processes the context using an open-source Large Language Model (LLM) via **Ollama**, and speaks the response back to you using a local text-to-speech engine.

---

## ✨ Features
* **100% Local & Private:** No data ever leaves your machine. No API tokens or cloud subscriptions required.
* **Completely Free:** Zero usage limits, rate limits, or surprise cloud computing bills.
* **Low Latency:** Uses an optimized, lightweight open-source model designed for near-instant responses.
* **Cross-Platform Audio Control:** Powered by modern, pre-compiled hardware layers that access mic arrays natively.

---

## 🛠️ Architecture Pipeline
1. **Speech-to-Text (STT):** Microphone audio is captured via `sounddevice` and transcribed using `SpeechRecognition`.
2. **LLM Engine (Brain):** The text query is processed locally using the **Llama 3.2 (1B)** model orchestrated by **Ollama**.
3. **Text-to-Speech (TTS):** The structured response is spoken out loud through system speakers using the offline `pyttsx3` driver layer.

---

## 🚀 Getting Started

### 1. Prerequisites
First, download and install **Ollama** on your computer from [ollama.com](https://ollama.com). 

Once installed, open your terminal/command prompt and pull the lightweight conversational model:
```bash
ollama run llama3.2:1b
```
*Note: You can close the window once the download completes. Ollama will keep running quietly in your background taskbar.*

### 2. Installation & Setup
Clone this repository to your local desktop workspace:
```bash
git clone https://github.com
cd "AI VOICE ASSISTANT"
```

Create and activate a isolated Python virtual environment to keep dependencies clean:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

Install the required open-source python packages:
```bash
pip install sounddevice scipy speechrecognition ollama pyttsx3 numpy
```

### 🏃 3. Running the Assistant
Launch the infinite listener loop script:
```bash
python main.py
```
* Speak your questions out loud into your microphone when you see `🎤 Recording...` appear. 
* Type `Ctrl + C` or say **"exit"** to safely terminate the program window.

---

## 📂 Project Structure
```text
├── venv/                 # Local python virtual environment (ignored by git)
├── main.py               # Principal continuous audio execution script
├── README.md             # Project roadmap and guide documentation
└── .gitignore            # Git exclusion mapping file
```

---

## 🛡️ License
Distributed under the MIT License. See `LICENSE` for more information.
