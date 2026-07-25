# 🎙️ Personal Voice Assistant

A Python-based Personal Voice Assistant that can understand voice commands, speak responses, fetch live weather information, read the latest news headlines, set reminders, and provide the current date and time.

---

## 📌 Features

- 🎤 Voice Recognition
- 🔊 Text-to-Speech Response
- 🌤 Live Weather Information
- 📰 Latest News Headlines
- ⏰ Reminder System
- 🕒 Current Time
- 📅 Current Date
- 🧠 Basic Natural Language Command Detection

---

## 🛠️ Technologies Used

- Python 3
- SpeechRecognition
- PyAudio
- pyttsx3
- Requests
- NewsAPI
- OpenWeatherMap API
- python-dotenv

---

## 📂 Project Structure

```text
Task 2 Voice_Assistant
│
├── assistant.py          # Main Voice Assistant
├── speech.py             # Speech Recognition & Text-to-Speech
├── weather.py            # Weather Module
├── news.py               # News Module
├── reminder.py           # Reminder Module
├── utils.py              # Text Normalization Utilities
├── config.py             # API Configuration
├── .env                  # API Keys
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/your-repository.git
```

Navigate to the project folder:

```bash
cd "Personal Voice Assistant"
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Setup

Create a `.env` file inside the project folder.

```env
WEATHER_API_KEY=your_openweathermap_api_key
NEWS_API_KEY=your_newsapi_key
```

### Get API Keys

- OpenWeatherMap → https://openweathermap.org/api
- NewsAPI → https://newsapi.org/

---

## ▶️ Run the Project

```bash
python assistant.py
```

---

## 🎤 Supported Voice Commands

### 🌤 Weather

- What is the weather today?
- Tell me the weather.
- Temperature in Vadodara.
- Weather forecast.

### 📰 News

- Tell me today's news.
- Latest headlines.
- Current news.

### ⏰ Reminder

- Set a reminder.
- Remind me to call John.
- Remind me after 10 seconds.

### 🕒 Time

- What time is it?
- Current time.

### 📅 Date

- What's today's date?
- Tell today's date.

### ❓ Help

- Help
- What can you do?

### 🚪 Exit

- Exit
- Quit
- Goodbye

---

## 📦 Requirements

- SpeechRecognition
- PyAudio
- pyttsx3
- requests
- python-dotenv
- newsapi-python

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🚀 Future Improvements

- AI Chat Support
- Wikipedia Search
- Music Playback
- Email Sending
- Alarm System
- Calculator
- Desktop GUI
- Offline Speech Recognition
- Integration with Large Language Models (LLMs)


---

## 📄 License

This project is open-source and intended for learning, experimentation, and educational purposes.
