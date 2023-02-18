import speech_recognition as sr
import pyttsx3 as tts
import datetime as dt
import webbrowser

engine = tts.init()
r = sr.Recognizer()

def takeCommand():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recongizing...")
            Query = r.recognize_google(audio, language="en-US")
        except Exception as e:
            print(e)
            print("Say that again please")
            return "None"
        
        return Query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tellDay():
    day = dt.datetime.today().weekday() +1

    Day_dict = {
        1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'
    }

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak(f"It is {day_of_the_week} today!")


def tellTime():
    time = str(dt.datetime.now())
    print(time)
    
    hour = time[11:13]
    if "0" in hour:
        hour = hour.split("0")
    min = time[14:16]
    speak(f"The time is {hour} hours and {min} minutes")

def openMail():
    webbrowser.open('mailto:', new=1)
    speak("I opened your mail for you.")

def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Sorry, I couldn't perform that calculation"


def voiceCalc():
    expression = takeCommand()
    result = calculate(expression)
    speak(f"{result}")