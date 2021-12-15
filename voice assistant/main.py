import speech_recognition as sr
import time
import string 
import pyttsx3




engine = pyttsx3.init()
mic = sr.Microphone()
r = sr.Recognizer()


#change default settings
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)


def listen_up():
    with mic as source:
            r.adjust_for_ambient_noise(source, duration = 0.5)
            audio = r.listen(source)
            r_str = r.recognize_google(audio)
    return(r_str)


def main_talk():
    engine.say("If you don't want to continue the conversation, just say 'exit'")
    engine.runAndWait()
    while True:
        rows = listen_up()
        print(rows)
        if rows == "exit":
            engine.say('Goodbye!!')
            engine.runAndWait()
            break
        elif rows == "hello" or rows == "hi":
            engine.say('Hello')
            engine.runAndWait()
        elif "time" in rows:
            engine.say(time.ctime())
            engine.runAndWait()

main_talk()
