# JARVIS: Python Voice Assistant

A desktop voice assistant inspired by Tony Stark's JARVIS from Iron Man. It listens through the microphone, works out what you asked, and answers out loud: it looks things up on Wikipedia, opens and searches websites, plays music and tells the time.

## Demo

**Answering questions from Wikipedia**

https://github.com/pranaylachuluri/JARVIS/assets/103355762/ea7caf0e-bcf3-44cf-b5a9-430153b06f4d

**Browser tasks (YouTube and Google search)**

https://github.com/pranaylachuluri/JARVIS/assets/103355762/056349d2-5a90-438e-8c0c-a99a7204e0a3

**Playing music**

https://github.com/pranaylachuluri/JARVIS/assets/103355762/1a54fc10-e2a4-40e7-aa4a-24ed67c43d2a

## Voice commands

| Say | What happens |
| --- | --- |
| "wikipedia &lt;topic&gt;" | Reads a two-sentence Wikipedia summary aloud |
| "open youtube" / "open google" | Opens the site in your browser |
| "&lt;query&gt; in youtube" / "search for &lt;query&gt; in google" | Searches the site for your query |
| "open &lt;site&gt; in browser" | Opens &lt;site&gt;.com |
| "play music" | Plays a song from your music folder |
| "the time" | Tells you the current time |
| "thank you" / "stop" / "quit" | Ends the session |

## How it works

1. **Listen**: `speech_recognition` records from the microphone and transcribes speech with Google's speech-to-text API.
2. **Understand**: the transcribed text is matched against keyword commands.
3. **Act**: `wikipedia`, `webbrowser` and `os` carry out the task.
4. **Speak**: `pyttsx3` reads the reply aloud with an offline text-to-speech voice and greets you by time of day on start-up.

## Tech stack

Python · SpeechRecognition · pyttsx3 · wikipedia · webbrowser · datetime · os

## Run it

```bash
pip install SpeechRecognition pyttsx3 wikipedia pyaudio
python jarvis.py
```

Built for Windows (it uses the SAPI5 voice and `os.startfile`). Before running, change `music_dir` in `jarvis.py` to a folder of songs on your computer.
