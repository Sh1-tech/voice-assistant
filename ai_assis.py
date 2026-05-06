import speech_recognition as sr 
import pyttsx3 
import pywhatkit
import wikipedia
import datetime
from gtts import gTTS
import os

r =sr.Recognizer()

def speak(command):
    tts = gTTS(text=command, lang='en', tld='com') 
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices') #collect
    engine.say(command)
    engine.runAndWait()
    tts.save("speech.mp3")

def commands(): #try and cach
    try:
        with sr.Microphone() as source: #microphone as input
            r.adjust_for_ambient_noise(source)
            print("Listening... Ask now...")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            print("You said:", text)

            #ask to play on youtube
            if "play" in text:
                text = text.replace("play", "")
                pywhatkit.playonyt(text)
                speak("Playing " + text + " on YouTube")
                return
            #ask date
            if 'date' in text:
                today = datetime.date.today()
                speak("Today's date is " + today.strftime("%Y-%m-%d"))
                return
            #ask time
            if 'time' in text:
                now = datetime.datetime.now()
                speak("The time now is " + now.strftime("%I:%M %p"))
                return

            #ask details about any person
            if "who is" in text:
                person = text.replace("who is","")
                info = wikipedia.summary(person,1)
                speak(info)
                return

            return text
    except:
        print("Error: Could not understand audio")
        return ""

speak("Hello I am a voice assistant created by Sharifa Al-Yousef. How can I help you?")

while True:
    result = commands()
    stop_words = ["goodbye", "bye", "stop", "quit", "exit"]
    if result and any(word in result for word in stop_words):
        speak("Goodbye! Have a great day!")
        break

