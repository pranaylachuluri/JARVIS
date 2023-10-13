import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
 
    speak("I am Jarvis sir, an AI assistant by Tony Stark, how may i help you?")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    a=True
    while a:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            try:
                print(results.encode("utf-8", errors="ignore").decode("utf-8"))
            except Exception as e:
                print("Failed to print results:", e)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'in youtube' in query:
            query= query.replace("in youtube", "")
            if 'open' in query:
                query= query.replace("open", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'in google' in query:
            query= query.replace("in google", "")
            if 'search for' in query:
                query= query.replace("search for", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif 'in browser' in query:
            query= query.replace("in browser", "")
            if 'open' in query:
                query= query.replace("open", "")
            webbrowser.open(f"{query}.com")
        elif 'play music' in query:
            music_dir='E:\\Sreya'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

        elif 'thank you' in query or 'quit' in query or 'stop' in query:
            speak("Happy that i could help, signing off")
            a=False

        



        










