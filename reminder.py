import threading
import time
from speech import speak


def reminder_task(message, seconds):
    time.sleep(seconds)

    print("\n" + "=" * 55)
    print("🔔 REMINDER")
    print("=" * 55)
    print(f"📌 {message}")
    print("=" * 55)

    speak(f"Reminder. {message}")


def set_reminder(message, seconds):
    thread = threading.Thread(
        target=reminder_task,
        args=(message, seconds)
    )

    thread.start()
    return thread