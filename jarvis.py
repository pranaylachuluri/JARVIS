import datetime
import os
import platform
import subprocess
import urllib.parse
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

# Folder that "play music" picks songs from; override with the JARVIS_MUSIC_DIR environment variable
MUSIC_DIR = os.environ.get('JARVIS_MUSIC_DIR', os.path.join(os.path.expanduser('~'), 'Music'))
AUDIO_EXTENSIONS = ('.mp3', '.wav', '.m4a', '.flac', '.ogg')

# pyttsx3 picks the right speech engine for the OS (SAPI5 on Windows, NSSpeechSynthesizer on macOS, eSpeak on Linux)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)


def speak(audio):
    print(f"Jarvis: {audio}")
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
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Say that again please")
        return "None"
    except sr.RequestError as e:
        print(f"Speech service unavailable: {e}")
        return "None"
    return query


def open_file(path):
    # os.startfile only exists on Windows
    if platform.system() == 'Windows':
        os.startfile(path)
    elif platform.system() == 'Darwin':
        subprocess.Popen(['open', path])
    else:
        subprocess.Popen(['xdg-open', path])


def search_wikipedia(query):
    speak('Searching Wikipedia...')
    topic = query.replace("wikipedia", "").strip()
    if not topic:
        speak("What should I look up on Wikipedia?")
        return
    try:
        results = wikipedia.summary(topic, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"{topic} could mean several things, for example {', '.join(e.options[:3])}. Please be more specific.")
        return
    except wikipedia.exceptions.PageError:
        speak(f"I couldn't find a Wikipedia page for {topic}.")
        return
    except Exception:
        speak("I couldn't reach Wikipedia right now.")
        return
    speak("According to Wikipedia")
    speak(results)


def play_music():
    if not os.path.isdir(MUSIC_DIR):
        speak("I couldn't find your music folder. Set JARVIS_MUSIC_DIR to the folder with your songs.")
        return
    songs = sorted(f for f in os.listdir(MUSIC_DIR) if f.lower().endswith(AUDIO_EXTENSIONS))
    if not songs:
        speak("There are no songs in your music folder.")
        return
    open_file(os.path.join(MUSIC_DIR, songs[0]))


if __name__ == "__main__":
    wishMe()
    a=True
    while a:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            search_wikipedia(query)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'in youtube' in query:
            query= query.replace("in youtube", "")
            if 'open' in query:
                query= query.replace("open", "")
            webbrowser.open("https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(query.strip()))
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'in google' in query:
            query= query.replace("in google", "")
            if 'search for' in query:
                query= query.replace("search for", "")
            webbrowser.open("https://www.google.com/search?q=" + urllib.parse.quote_plus(query.strip()))
        elif 'in browser' in query:
            query= query.replace("in browser", "")
            if 'open' in query:
                query= query.replace("open", "")
            site = query.strip().replace(" ", "")
            webbrowser.open(f"https://{site}.com")
        elif 'play music' in query:
            play_music()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'thank you' in query or 'quit' in query or 'stop' in query:
            speak("Happy that i could help, signing off")
            a=False
