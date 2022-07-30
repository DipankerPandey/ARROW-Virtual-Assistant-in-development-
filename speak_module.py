import os

from gtts import gTTS
from playsound import playsound


def speak(text):
    text = str(text)
    text2 = text.replace("assistant", "assisstent")
    tts = gTTS(text2)
    tts.save('speech.mp3')
    playsound('speech.mp3')
    os.remove('speech.mp3')


