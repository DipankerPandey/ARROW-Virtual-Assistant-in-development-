from details import name
from speak_module import speak
from database import speak_is_on

def output(o):

    # command line output

    if speak_is_on():
        speak(o)
    else:
        print(name + ": " + o)
        print()
