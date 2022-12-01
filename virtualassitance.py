import pyttsx3
import datetime
import speech_recognition as sr



engine = pyttsx3.init()
#it is used to set voice according to us
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
#for voice speed by deafualt it is 200
newVoiceRate = 190
engine.setProperty('rate',newVoiceRate)

#fuction convert text to speech

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak('hey how are guys , Im zany  robo')


#here with the help of datetime pc speak current time
def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("the current time is"+time)

time()


#for curent dae using year month and day
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is:")
    speak(day)
    speak(month)
    speak(year)


date()



#greet us

def wishme():
    speak("welcome !")
    date()
    time()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("good morning")
    elif hour >=12 and hour <=18:
        speak('goof afternoon')
    elif hour>=18 and hour <=24:
        speak("good evening")
    else:
        speak('good night')

    speak("zany at your service . how can i help you?")

wishme()


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold  = 1
        audio = r.listen(source)

    try:
        print("recognizing")
        query = r.recognize_google(audio,'en-US')
        print(query)

    except Exception as e:
        print(e)
        speak("say, that again please")
        return "None"
    return query



takecommand()

