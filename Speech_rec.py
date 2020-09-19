import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')#for using default voice by microsoft
voices= engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour <18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello There!I'm Your Virtual Assistant.How may I help you? ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try: 
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f'Your said: {query}\n')

        except Exception as e:
            
            print("Can't Recognise!")
            return 'None'

        return query


if __name__ == "__main__":
    greetings()
    #while True:
    if 1:
        query = takeCommand().lower()

        #logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query= query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            #print(result)
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("googele.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open instagram" in query:
            webbrowser.open("instagram.com")

        elif "play music" in query:
            webbrowser.open("spotify.com")   

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir! The time is {strTime}')


        


    