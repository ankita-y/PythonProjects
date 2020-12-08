import io
import pygame
import os
from gtts import gTTS

def speech(text):
    try:
        audio = gTTS(text=text,lang="en")
        audio.save("text.wav")
        os.system("text.wav")
    except Exception as e:
        print("Exception: ",e)
    

if __name__ == '__main__':
    print("What should I say")
    text = input(" >> ")
    speech(text)
