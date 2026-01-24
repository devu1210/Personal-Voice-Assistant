# Personal-Voice-Assistant

A simple **rule-based personal voice assistant** built using Python.  
It listens to voice commands, converts speech to text, maps commands to predefined actions, and responds using text-to-speech.

This project demonstrates **Speech-to-Text (STT)**, **Text-to-Speech (TTS)**, and basic automation using voice commands.

---

## 🚀 Features

- 🎧 Speech-to-Text using **Google Speech Recognition**
- 🔊 Text-to-Speech using **gTTS**
- 🌐 Open websites (Google, YouTube)
- 🔍 Search the web via voice
- ⏰ Tell current time
- 📸 Take screenshots
- ❌ Exit assistant using voice
- ⚠️ Basic error handling for speech failures

---

Microphone Input
↓
Speech Recognition (STT)
↓
Rule-Based Command Mapping
↓
Action Execution
↓
Text-to-Speech Response (TTS)


This assistant is **rule-based**, not AI or NLP-based.

---

## 🛠️ Tech Stack

- Python 3.8+
- speech_recognition
- gTTS
- sounddevice
- pydub
- winsound (Windows only)
- pyautogui
- webbrowser
- numpy

⚠️ This project currently works on **Windows only** due to `winsound`.

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/personal-voice-assistant.git
cd personal-voice-assistant
```
2️⃣ Install dependencies
```bash
pip install SpeechRecognition gTTS pydub sounddevice numpy pyautogui
```
3️⃣ Install FFmpeg (Required)
```bash
pydub requires FFmpeg.

Download: https://ffmpeg.org/download.html

Add FFmpeg to system PATH
```
▶️ Usage
```bash
Run the assistant:

python assistant.py
```

The assistant will start listening for commands.

## 🧠 How It Works

🗣️ Sample Voice Commands

| Command           | Action             |
| ----------------- | ------------------ |
| `tell time`       | Tells current time |
| `open google`     | Opens Google       |
| `open youtube`    | Opens YouTube      |
| `search python`   | Searches Google    |
| `take screenshot` | Saves screenshot   |
| `exit` / `stop`   | Exits assistant    |


Speak clearly for best results.


