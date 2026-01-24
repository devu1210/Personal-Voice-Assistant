import speech_recognition as sr
from gtts import gTTS
import winsound
from pydub import AudioSegment
import pyautogui
import webbrowser
import datetime
import os
import sounddevice as sd
import numpy as np

recognizer = sr.Recognizer()
sr.Microphone = sr.Microphone

# ------------------ TTS ------------------
def respond(text):
    print("Assistant:", text)
    try:
        tts = gTTS(text=text)
        tts.save("reply.mp3")
        sound = AudioSegment.from_mp3("reply.mp3")
        sound.export("reply.wav", format="wav")
        winsound.PlaySound("reply.wav", winsound.SND_FILENAME)
    except Exception as e:
        print("Audio Error:", e)

# ------------------ STT ------------------

def listen_for_command():
    respond("Listening")
    duration = 5  # seconds
    samplerate = 16000

    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()

    audio_data = sr.AudioData(recording.tobytes(), samplerate, 2)

    try:
        command = recognizer.recognize_google(audio_data).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        respond("Sorry, I did not understand that.")
    except sr.RequestError:
        respond("Speech service is unavailable.")
    return ""

# ------------------ Command Processing ------------------
def process_command(command):

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        respond(f"The time is {time}")

    elif "open youtube" in command:
        respond("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        respond("Opening Google")
        webbrowser.open("https://google.com")

    elif "search" in command:
        query = command.replace("search", "").strip()
        respond(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "take screenshot" in command:
        pyautogui.screenshot("screenshot.png")
        respond("Screenshot saved successfully")

    elif "exit" in command or "stop" in command:
        respond("Goodbye")
        exit()

    else:
        respond("Sorry, I don't know how to do that yet")

# ------------------ Main Loop ------------------
def main():
    respond("Personal Voice Assistant Activated")

    respond("Sample commands: tell time, open google, open youtube, search python, take screenshot, exit")

    while True:
        command = listen_for_command()
        if command:
            process_command(command)

# ------------------ Start Program ------------------
if __name__ == "__main__":
    main()
