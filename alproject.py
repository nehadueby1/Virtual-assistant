import pyttsx3
from plyer import notification
import datetime
import wikipedia
import smtplib
import webbrowser as wb
import os
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

    speak("I am zara  at your service. how can i help you?")



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
        query = input()


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
            speak("i am zara robot i can help you in many ways ")


        #here we use wikipedia to search our query
        elif 'wikipedia' in query:
            speak("searching....")
            speak("what should i search ")
            query = input().replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak(result)

        elif 'sendemail' in query:
            try:
                speak("what should the content")
                to = 'xyz@gmail.com'
                content=input()
               # sendmail(to,content)
                speak(content)

            except Exception as e:
                speak(e)
                speak('unable to send email please try latter')
                print("unable to send")



        elif "search in chrome" in query:
            speak("what should i  search")
            search = input()
            wb.open_new(search+".com")

        elif "open python" in query:
            speak("okay")
            wb.open_new("python")



        #for logout restart and shutdown
        elif "log out" in query:
            os.system("shutdown - l")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        #for notification
        elif  "notify me" in query:
            speak("do you want to start ?")
            question = input()
            if 'yes' in question:
                speak("i am starting")
            if 'no' in question:
                speak("we will automatically start after 5 mins")
                time.sleep(5 * 60)
                speak("we are starting ")

            while True:
                notification.notify(title="let's start ",
                                    message=" we will tell to take a break after 5 minuts ",
                                    timeout=10)
                time.sleep(0.5 * 60)
                speak("please take a break sir")
                notification.notify(title="break notification",message=" please do use your device after sometime as you have been continuously using it for 45 mins and it will affect our eye",timeout=10)

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
            data = input()
            speak("you said me to remember" +data)
            remember = open("data.txt",'w')
            remember.write(data)
            remember.close()


        #which i said to remember my robo speak it
        elif "do you know anything" in query:
            remember=open("data.txt","r")
            speak("you said me to remember that"+remember)
