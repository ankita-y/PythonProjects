import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        speak("Good Morning!")
    elif hour>12 and hour <=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Luna. Your personal assistant. Please tell me how may I help you")

def takeCommand():
    '''It take microphone input and return string output'''
    rObject = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rObject.pause_threshold = 2
        audio = rObject.listen(source)
    try:
        print("Recognizing...")
        query = rObject.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Could not understand what you said, Please try again !")
        return "None"
    return query

#Take the query from the user and perform the operation
def process_Query(query):
    try:
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            webbrowser.open("https://www.wikipedia.org/")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'github' in query:
            webbrowser.open("https://github.com/")
        elif 'excel' in query:
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk')
        elif 'who made you' in query or "created you" in query:
            speak("I have been created by Ankita Yadav.")
        elif 'who are you' in query:
            speak("Hi, I am Luna. Your Personal Assistant. I am here to make your day to day work easy.")
    except:
        speak("Could not understand what you said, Please try again !")

if __name__ == '__main__':
    wishMe()
    while(1):
        query = takeCommand().lower()

        if "exit" in str(query) or "bye" in str(query) or "sleep" in str(query):
            speak("Ok Bye, Talk to you later")
            break
        process_Query(query)

