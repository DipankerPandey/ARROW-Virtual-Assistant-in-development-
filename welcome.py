from time_module import get_hours, get_date
from database import put_last_seen, get_last_seen
from speak_module import speak

def greet():
    previous_date = get_last_seen()

    today_date = get_date()
    if previous_date == today_date:
        put_last_seen(today_date)
        speak("Welcome back")
        return "Welcome back"
    else:
        put_last_seen(today_date)
        hour = int(get_hours())

        if 5 <= hour < 12:
            speak("Good morning")
            return "Good morning"
        elif 12 <= hour < 16:
            speak("Good afternoon")
            return "Good afternoon"
        else:
            speak("Good evening")
            return "Good evening"