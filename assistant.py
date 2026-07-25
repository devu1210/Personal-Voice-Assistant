from datetime import datetime
import re

from speech import speak, listen
from weather import get_weather
from news import get_news
from reminder import set_reminder
from utils import normalize


# Supported Intents

INTENTS = {

    "weather":[
        "weather",
        "temperature",
        "forecast",
        "rain",
        "climate",
        "how is weather",
        "what is weather",
        "weather today",
        "tell weather"
    ],

    "news":[
        "news",
        "headlines",
        "latest news",
        "today news",
        "tell news",
        "current affairs"
    ],

    "time":[
        "time",
        "what time",
        "current time",
        "clock"
    ],

    "date":[
        "date",
        "today",
        "today date",
        "what is today"
    ],

    "help":[
        "help",
        "assist",
        "commands",
        "what can you do"
    ],

    "reminder":[
        "reminder",
        "alarm",
        "notify",
        "remind me"
    ],

    "exit":[
        "exit",
        "quit",
        "bye",
        "goodbye",
        "close"
    ]
}



# Intent Detection


def detect_intent(command):
    for intent, keywords in INTENTS.items():
        if any(keyword in command for keyword in keywords):
            return intent
    return "unknown"



# Weather

def handle_weather():
    speak("Which city would you like to know the weather for?")

    city = normalize(listen())

    if not city:
        speak("I couldn't understand the city name.")
        return

    weather = get_weather(city)

    if not weather:
        speak("Sorry, I couldn't fetch the weather right now.")
        return

    weather_text = (
        f"Weather in {weather['city']}, {weather['country']}. "
        f"Temperature is {weather['temperature']} degrees Celsius. "
        f"It feels like {weather['feels_like']} degrees. "
        f"Humidity is {weather['humidity']} percent. "
        f"Condition is {weather['description']}. "
        f"Wind speed is {weather['wind']} meters per second."
    )

    print("\n" + "=" * 60)
    print("🌤 WEATHER REPORT")
    print("=" * 60)
    print(weather_text)
    print("=" * 60)

    speak(weather_text)



# News


def handle_news():
    headlines = get_news()

    if not headlines:
        speak("Sorry, I couldn't fetch the latest news.")
        return

    print("\n" + "=" * 60)
    print("📰 TODAY'S TOP HEADLINES")
    print("=" * 60)

    speak("Here are today's top headlines.")

    for i, article in enumerate(headlines, start=1):
        title = article.get("title", "Untitled headline")
        source = article.get("source", {}).get("name", "Unknown source")
        published_at = article.get("publishedAt", "")

        line = f"{i}. {title}"
        if source:
            line += f" ({source})"
        if published_at:
            line += f" - {published_at[:10]}"

        print(line)
        speak(title)

    print("=" * 60)



# Reminder


def handle_reminder():
    speak("What should I remind you about?")

    message = listen()

    if not message:
        speak("Reminder cancelled.")
        return

    speak("After how many seconds?")

    seconds_text = normalize(listen())
    match = re.search(r"\d+", seconds_text)

    if not match:
        speak("Please say a valid number.")
        return

    seconds = int(match.group())

    if seconds <= 0:
        speak("Please provide a number greater than zero.")
        return

    set_reminder(message, seconds)

    print("\n✅ Reminder Set Successfully!\n")

    speak("Your reminder has been set.")



# Time


def handle_time():
    current_time = datetime.now().strftime("%I:%M %p")

    print("\n🕒 Current Time :", current_time)

    speak(f"The current time is {current_time}")



# Date


def handle_date():
    current_date = datetime.now().strftime("%d %B %Y")

    print("\n📅 Today's Date :", current_date)

    speak(f"Today is {current_date}")



# Help


def show_help():
    print("\n" + "=" * 60)
    print("📚 AVAILABLE COMMANDS")
    print("=" * 60)

    print("""
🌤 Weather
📰 News
⏰ Reminder
🕒 Time
📅 Date
❓ Help
🚪 Exit
""")

    print("=" * 60)

    speak("These are the commands I support.")



# Welcome Screen


def show_banner():
    print("=" * 60)
    print("🤖VOICE ASSISTANT")
    print("=" * 60)

    print("""
Welcome!

I can help you with:

🌤 Weather
📰 Latest News
⏰ Reminders
🕒 Current Time
📅 Today's Date

Say 'Help' anytime to view all commands.
""")

    print("=" * 60)

    speak("Hello there, I am your personal voice assistant. How can I help you today?")



# Main Program


def main():

    show_banner()

    while True:

        print("\n🎤 Listening...")

        command = normalize(listen())

        if not command:
            continue

        intent = detect_intent(command)

        if intent == "weather":
            handle_weather()

        elif intent == "news":
            handle_news()

        elif intent == "reminder":
            handle_reminder()

        elif intent == "time":
            handle_time()

        elif intent == "date":
            handle_date()

        elif intent == "help":
            show_help()

        elif intent == "exit":
            speak("Goodbye. Have a wonderful day.")
            print("\n👋 Assistant Closed Successfully.")
            break

        else:
            speak("Sorry, I don't know how to help with that.")
            print("❌ Unknown command.")



# Entry Point


if __name__ == "__main__":
    main()