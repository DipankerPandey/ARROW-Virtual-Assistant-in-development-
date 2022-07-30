import speech_recognition as sr
from database import turn_off_name_said, turn_on_name_said, listen_command
from output_module import output


def get_audio():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            if not listen_command():
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=8, phrase_time_limit=8)
                said = r.recognize_google(audio, language="en-GB")
                if "computer" in str(said).lower() or "arrow" in str(said).lower() or "aro" in str(said).lower():
                    turn_on_name_said()
                    output("listening...")

                else:
                    return get_audio()

            if listen_command():
                audio = r.listen(source, timeout=8, phrase_time_limit=8)
                comm = r.recognize_google(audio, language="en-GB")
                turn_off_name_said()
                if comm != "":
                    return comm
                return get_audio()

    except Exception:
        output(r"I can't hear you")
        return get_audio()
