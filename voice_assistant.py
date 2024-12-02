import pyttsx3 as sx
import speech_recognition as sr
import pyaudio
import webbrowser
import datetime

import os
import smtp2zope

#speech to text funtion using speech_recognition and pyaudio module
def get_pyaudio():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Recognizing.......")
            data =recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understand")
#get_pyaudio()

#text to speech funtion using pyttsx3 module
def specch_tx(x):
    engin=sx.init()
    voices=engin.getProperty('voices')
    engin.setProperty('voice',voices[1].id)#0 number is voice of male and 1 number is voice of female
    rate=engin.getProperty('rate')
    engin.setProperty('rate',150)
    engin.say(x)
    engin.runAndWait()
#specch_tx("hello My Name is Prachi Kesarwani")

if __name__=='__main__':


    #if get_pyaudio().lower() =="Hey Peter":
        while True:
            data1=get_pyaudio().lower()
            if "your name" in data1:
               name="My name is Peter. My mission is assist you."
               print(name)
               specch_tx(name)

            elif "old are you" in data1:
               age="I am 20 years old "
               print(age)
               specch_tx(age)

            elif "time" in data1:
               time= datetime.datetime.now().strftime("%I:%M:%p")
               print(time)
               specch_tx(time)

            elif "date" in data1:
               date=datetime.datetime.now().strftime("%d:%m:%y:%a")
               print(date)
               specch_tx(date)

            elif "animation" in data1:
               webbrowser.open("https://www.youtube.com/@Ptechanimation-78")
            elif "youtube" in data1:
               webbrowser.open("https://www.youtube.com/")
            elif "translate" in data1:
               webbrowser.open("https://translate.google.com/")
            elif "google" in data1:
               webbrowser.open("https://www.google.com/")

            
            #elif "play song" in data1:

            elif "exit" in data1:
                specch_tx("Thank you")
                break







