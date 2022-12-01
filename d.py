import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("I am your Alexa")
engine.say("What I do for you")
engine.runAndWait()
try:
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source, duration=1)
        print("Listening.....")

        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)
except Exception as e:
    print("exception",e)