from database import hearing
from listen_module import get_audio


def take_input():
    if not hearing():
        i = input("You: ")
        return i

    else:
        i = str(get_audio())
        print("You: " + i)
        return i
