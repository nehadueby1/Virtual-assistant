import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
from plyer import notification
import psutil


engine = pyttsx3.init()

#it is used to set voice according to us
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#for voice speed by deafualt it is 200
newVoiceRate = 190
engine.setProperty('rate',newVoiceRate)

#fuction convert text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



#here with the help of datetime pc speak current time
def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("the current time is"+time)



#for curent dae using year month and day
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is:")
    speak(day)
    speak(month)
    speak(year)





#greet us
def wishme():
    speak("Your most welcome !")
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("good morning have a wonderful day")
    elif hour >=12 and hour <=18:
        speak('good afternoon have a cheerful noon ')
    elif hour>=18 and hour <=24:
        speak("good evening have a surprising evening ")
    else:
        speak('good night sweet dreams ')

    speak("I am zaara  at your service. how can i help you?")


#takecommand  from using microphone class in sr it take the microphone input from user and returns srtring output
def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening")
        #r.pause_threshold  = 1
        audio = r.listen(source)

    try:
        print("recognizing")
        query = r.recognize_google(audio)
        print(query)

    except Exception as e:
        speak("say, that again please")
        return "None"
    return query

#sending email
def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.echlo()
    server.starttls()
    server.login('nehadubey@gmail.com','text456')
    server.sendmail('nehadubey@gmail.com',to,content)
    server.close()


#for screenshot we have to def a fuction
#def screenshot():
    #img = pyautogui.screenshot()
    #img.save("C:\Users\Neha Dubey\Desktop\pythonss\ss.png")




if __name__ == "__main__":

    wishme()

    while True:
        query = takecommand().lower()
        print(query)

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif "offline" in query:
            speak("Thank for your time. I am quiting")
            quit()

        elif "who are you" in query:
            speak("hello i am zaara robot ")

        elif "what are you doing" in query:
            speak("hey i am just following your command what about you")

        elif "nothing" in query:
            speak("Okay how can I help you ")

        elif "how are you" in query:
            speak("i am good thank you how are you")

        elif "tell me something about you" in query:
            speak("i am zaara robot i can help you in many ways ")

        #here we use wikipedia to search our query
        elif 'wikipedia' in query:
            speak("searching....")
            speak("what should i search ")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak(result)

        elif 'sendemail' in query:
            try:
                speak("what should the content")
                content = takecommand()
                to = 'xyz@gmail.com'
               # sendmail(to,content)
                speak(content)

            except Exception as e:
                speak(e)
                speak('unable to send email')

        elif "search in chrome" in query:
            speak("what should i  search")
            search = takecommand().lower()
            chrom ="google.com"
            text = "https://www.google.com/search?source=hp&ei=X6dPX4CfE86b9QOJ3ruwDw&q="+search
            wb.get(chrom).open_new_tab(text)

        #for logout restart and shutdown
        elif "log out" in query:
            os.system("shutdown - l")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        #for notification
        elif  "notify me" in query:
            notification.notify(title="hi it's zaara", message="now you have to take a break your zaara need a break", timeout=2)
            time.sleep(7)

        #for remaining battery %
        elif "battery" in query:
            battery = psutil.sensors_battery()
            print("Battery percentage:", battery.percent, "%")
            print("power plugged in:", battery.power_plugged)

        #for playing songs using os module
        elif "play song" in query:
            songs_dir = ""
            songs=os.listdir(songs_dir)
            os.startfile(songs_dir,songs[0])

        #this is for remember the things which i want to
        elif "remember " in query:
            speak("what should i remember")
            data = takecommand()
            speak("you said me to remember" +data)
            remember = open("data.txt",'w')
            remember.write(data)
            remember.close()

        #which i said to remember my robo speak it
        elif "do you know anything" in query:
            remember=open("data.txt","r")
            speak("you said me to remember that"+remember.read())

        #for taking screenshot
