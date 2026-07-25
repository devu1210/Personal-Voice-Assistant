try:
    import pyttsx3
except ImportError:
    pyttsx3 = None

try:
    import speech_recognition as sr
except ImportError:
    sr = None


def speak(text):
    print(f"Assistant: {text}")

    if pyttsx3 is None:
        return

    engine = pyttsx3.init()
    engine.setProperty("rate", 170)

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

    del engine



def listen():
    if sr is None:
        typed = input("⌨ Type your command: ")
        return typed.lower()

    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 1.0
    recognizer.operation_timeout = 5

    try:
        with sr.Microphone() as source:
            print("\n🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            try:
                audio = recognizer.listen(
                    source,
                    timeout=8,
                    phrase_time_limit=8
                )
            except sr.WaitTimeoutError:
                print("⌛ No speech detected.")
                return ""

        try:
            command = recognizer.recognize_google(audio)
            print(f"👤 You: {command}")
            return command.lower()

        except sr.UnknownValueError:
            print("❌ Couldn't understand.")

        except sr.RequestError:
            print("🌐 Internet connection problem.")

    except OSError as e:
        print("🎙 Microphone unavailable:", e)

    except Exception as e:
        print("Speech Error:", e)

    typed = input("⌨ Type your command (or press Enter to retry): ")
    return typed.lower()