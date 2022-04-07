import sys
import os
import pyttsx3 #pip install pyttsx3
import pywhatkit #pip install pywhatkit
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import smtplib
import pyautogui #pip install pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)

def command_error():
    speak("Sorry, My version need to be updated. Can't recognize command.")
    main()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 600
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Voice Received: {query}\n")

    except Exception as e:    
        command_error() 
        return "None"
    return query

def noCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 600
        audio = r.listen(source)
    try:
        query2 = r.recognize_google(audio, language='en-in')
    except:
        return "none"
    return query2

def Greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening SIr !")  

    speak("How can I help") 
    main()

def start_ai():
    os.system('cls')
    os.system('color a')
    print("\t\t\t\t\t Dot-Matrix Status: Online")
    Greeting()

def resume():
    print("\t\t\t\t\t Dot-Matrix Status: Online")
    speak('Hello Sir, I am listening')
    main()

def pause():
    print("\t\t\t\t\t Dot-Matrix Status: Offline")
    speak('Listening Disabled, until you wake me up !')
    while True:
        command = noCommand().lower()
        if 'wake up' in command or 'start listening' in command or 'hey matrix' in command or 'where are you' in command or 'are you there' in command:
            resume()

        elif 'shutdown' in command or 'go offline' in command:
            exit()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('myemail@gmail.com', 'pswd')
    server.sendmail('myemail@gmail.com', to, content)
    server.close()

def youtube_search(term):
    search = "https://www.youtube.com/results?search_query=" + term
    webbrowser.open(search)
    speak("This is what I found Sir")
    pywhatkit.playonyt(term)
    speak("First video might be helpfull")
    pause()

def google_search(term):
    search = "https://www.google.com/search?q=" + term
    webbrowser.open(search)
    speak("This is what I found in google")
    pause()

def open_url(query):
    query1 = query.replace("open","")
    query2 = query1.replace("in browser","")
    term = query2.replace(" ","")
    if (term == ""):
        speak('What should I open ?')
        term = takeCommand()
    speak (f"Sure sir, Opening {term}")
    webbrowser.open(f'http://www.{term}.com')
    pause()

def exit():
    speak("Startup Application Shutdown Sequence. Goodbye Sir ")
    os.system('color 7')
    sys.exit()

def main():
    while True:
        query = takeCommand().lower()

        if 'hey dot matrix' in query or 'hey matrix' in query or 'hello' in query:
            speak('Hey, Sugam. How can I help')

        elif 'what can you do' in query:
            speak('Just tell me what i have to do')

        elif 'where do you live' in query or 'your home' in query or 'where are you from' in query:
            speak('I live in my virtual world created by my developer')

        elif 'introduce yourself' in query or 'introduction' in query or "your name" in query or 'who are you' in query or 'who made you' in query or 'who is your developer' in query:
            speak('Hi, I am your Virtual AI, Dot Matrix. I am being developed by Sugam and still in beta version.')

        elif 'wikipedia' in query or 'who is' in query or 'what is' in query or 'meaning' in query or 'mean by' in query:

            if 'my ip address' in query or 'my address' in query or 'my ip' in query:
                from requests import get
                ip = get('http://api.ipify.org').text
                print (f"Your IP adress is: {ip}")
                speak (f"Your IP adress is: {ip}")
                main()

            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                query = query.replace("what is", "")
                query = query.replace("who is", "")
                query = query.replace("meaning", "")
                query = query.replace("search", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                command_error()

        elif 'google search' in query or 'search' in query:
            term = query.replace("google search","")
            term = query.replace("search","")
            google_search(term)

        elif 'on youtube' in query or 'in youtube' in query:
            term1 = query.replace("play","")
            term2 = term1.replace("open","")
            term3 = term2.replace("in youtube","")
            term = term3.replace("on youtube","")
            print(term)
            youtube_search(term)

        elif 'open browser' in query or 'in browser' in query or 'open' in query:
            open_url(query)
        
        elif 'close browser' in query:
            os.system("TASKKILL /F /im msedge.exe")
            speak ("Browser Closed")

        elif 'play music' in query or 'play songs' in query or 'play my favourite' in query:
            speak ("Sure sir, playing your favourite song library")
            webbrowser.open("https://www.youtube.com/watch?v=mS60nG6bJwo&list=RDmS60nG6bJwo&start_radio=1")
            pause()
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'send email' in query or 'send a mail' in query or 'email' in query:
            try:

                speak("What should I say?")
                content = takeCommand()
                to = "nsugam248@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'who am i' in query or 'what is my name' in query:
            speak("Your are my developer, Sugam")

        elif 'volume up' in query:
            for i in range (5):
                pyautogui.press('volumeup')
            speak ("Volume Increased by 5")

        elif 'volume down' in query:
            for i in range (5):
                pyautogui.press('volumedown')
            speak ("Volume is Down by 5")

        elif 'mute volume' in query or 'mute volume' in query:
            pyautogui.press('volumemute')
            print ("Volume Muted")

        elif 'delete conversation' in query:
            print("Are you sure you want to delete our conversations ?")
            speak("Are you sure you want to delete our conversations ?")
            ask = takeCommand().lower()
            if 'yes' in ask or 'sure' in ask:
                speak("Deleting the conversation.\nPlease wait...")
                os.system('cls')
                start_ai()
            elif 'no' in query:
                speak("Ok Sir")

        elif 'stop listening' in query or 'go offline' in query:
            pause()

        elif 'shutdown' in query:
            if 'system' in query:
                os.system('shutdown /s')
            exit()
       
        elif 'restart system' in query:
            os.system('shutdown /r')
            exit()

        else:
            command_error()

start_ai()
