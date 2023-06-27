# DeskAssistant

This is still under construction. If you find any errors report them in the 'issues' tab in the github at: https://github.com/Blinken77YT/DeskAssistant/issues

This project was developed by Theo Nilsson, Blinken77YT (c) 2023

## Examples of How To Use

Creating a 'Assistant'

```python
from deskAssistant import Assistant

ai = Assistant()
```

Heres how you can use it to take a query and provide a response based on it
```python
from deskAssistant import Assistant

ai = Assistant()

while True:
    query = ai.takeCommand().lower()
    if query in ["hello", "hi", "sup", "whats up", "what's up", "what is up"]:
        ai.speak("Hello!")
    elif query == "open my mail":
        ai.openMail()
    else:
        ai.speak("What did you say? I didn't understand")
```

## Here are some other features
```python
ai.takeCommand() # Listens for users speech
ai.speak(text) # Says the text specified in the parameters
ai.tellDay() # Says the day
ai.tellTime() # Tells the time
ai.openMail() # Opens your mail
ai.calculate() # A basic calculate function
ai.voiceCalc() # A calculator taking input via your voice. Uses ai.calculate()
```

Check out my youtube: https://www.youtube.com/@blinken77