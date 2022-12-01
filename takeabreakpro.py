import pyttsx3
from plyer import notification
import time


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def take_break():
    speak("do you want to start ?")
    question = input("do")
    if 'yes' in question:
        speak("i am starting")
    if 'no' in question:
        speak("we will automatically start after 5 mins")
        time.sleep(5 * 60)
        speak("we are starting ")

    while True:
        notification.notify(title="let's start ",
                            message="we will tell to take a break after 5 minuts",
                            timeout=10)
        time.sleep(0.5 * 60)
        speak("please take a break sir")
        notification.notify(title="break notification",
                            message="please do use your device after sometime as you have been continuously using it for 45 mins and it will affect our eye",
                            timeout=10)

if __name__ == "__main__":
    take_break()

