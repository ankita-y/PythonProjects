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
        """gTTS(text=text,lang="en").write_to_fp(file)
        file.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
"""


if __name__ == '__main__':
    print("What should I say")
    text = input(" >> ")
    speech(text)