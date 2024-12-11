from tkinter import mainloop
from xml.sax import make_parser
from tkinter import *
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from flask import Flask
import pywhatkit
import random
import smtplib
import pyjokes



passwrd = "rahulsingh"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning maam")
    elif hour>=12 and hour<18:
        speak("Good Afternoon maam")
    else:
        speak("Good Evening maam")

    speak("I am Spark. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("user said:" , query)

    except Exception as e:
        print(e)

        print("Say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.ehlo()
    server.login('fggghhsingh61@gmail.com',passwrd)
    server.sendmail('fggghhsingh61@gmail.com', to, content)
    server.close()

def run_spark():
    command= takeCommand()
    print(command)

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching Wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")
        elif 'marry' in query:
            speak("i am already married with siri,and i have son named bixby")
        elif 'play' in query:
            query = query.replace("play","")
            rd = ("playing", query)
            speak(rd)
            pywhatkit.playonyt(query) 
        elif 'open' in query:

            query = query.replace("open","")
            ur = 'https://www.google.com/search?q='+query+'&aqs=chrome'
            webbrowser.get().open(ur)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(strTime)
            speak(f"sir, the Time is{strTime}")
        elif 'your name' in query:
            speak("my name is spark")
        elif 'date' in query:
            strTime = datetime.datetime.now().strftime("%D:%M:%Y")
            print(strTime)
        elif 'alarm' in query:
            speak("alarm set successfully")
            print("alarm set successfully")

        elif 'jokes' in query:
            speak(pyjokes.get_jokes())
        elif 'find my location' in query:
            loca = ("What is my location")
            url = 'https://google.nl/maps/place/'+loca+'/&amp;'
            webbrowser.get().open(url)
            speak('Here is location'+loca)
        elif 'meaning' in query:
            url = 'https://www.google.com/search?q='+query+'&aqs=chrome'
            webbrowser.get().open(url)
            speak('Here is the result for'+query)


        elif 'email to rahul' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "nidhu2438@gmail.com" 
                sendEmail(to,content)
                print("email has been sent")
                speak("Email has been sent")
            except Exception as e:
                # print(e)
                speak("sorry sir, i am not able to send email at the moment")    
#
