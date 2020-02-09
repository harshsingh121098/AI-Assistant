import pyttsx3
import datetime
import speech_recognition as sr

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# 1 for girl and 0 for boy
#print(voices[1].id) #if you wish to tell which file is used to speak
engine.setProperty('voice',voices[0].id)


#speak function
def speak(audio):
    #for i in range(1,5): taki baar baar sunai deta rahe
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis sir , Ready at your command . Tell me what to do")

def takeCommand ():
    #it take mic input and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print("User said: {query}\n")

    except Exception as e:
        #print(e) #this prints the error
        print("Say that again plz")
        return "None"
    return query 



if __name__ == "__main__":
    #speak("Hello there") #for testing of program
    wishMe()
    takeCommand()