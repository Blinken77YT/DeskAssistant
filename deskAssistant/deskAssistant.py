import speech_recognition as sr
import pyttsx3 as tts
import datetime as dt
import webbrowser

class Assistant:
    def __init__(self, voiceid=0, rate=100):
        self.engine = tts.init()
        self.r = sr.Recognizer()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[voiceid].id)
        self.engine.setProperty('rate', rate)

    def takeCommand(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.r.pause_threshold = 0.7
            audio = self.r.listen(source)
            try:
                print("Recongizing...")
                Query = self.r.recognize_google(audio, language="en-US")
            except Exception as e:
                print(e)
                print("Say that again please")
                return "None"
            
            return Query

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def tellDay(self):
        day = dt.datetime.today().weekday() +1

        Day_dict = {
            1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'
        }

        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
            self.speak(f"It is {day_of_the_week} today!")


    def tellTime(self):
        time = str(dt.datetime.now())
        print(time)
        
        hour = time[11:13]
        if "0" in hour:
            hour = hour.split("0")
        min = time[14:16]
        self.speak(f"The time is {hour} hours and {min} minutes")

    def openMail(self):
        webbrowser.open('mailto:', new=1)
        self.speak("I opened your mail for you.")

    def calculate(self, expression):
        try: 
            result = eval(expression)
            return str(result)
        except:
            return "Sorry, I couldn't perform that calculation"


    def voiceCalc(self):
        expression = self.takeCommand()
        result = self.calculate(expression)
        self.speak(f"{result}")