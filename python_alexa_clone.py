import pyttsx3
import pywhatkit
import datetime
import speech_recognition as sr
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(r'Hi i am anshs assistant ')
engine.say('what can i do for you?')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as saurce:
            print('mai sun raha hu...')
            voice = listener.listen(saurce)
            command = listener.recognize_google(voice)
            command = command.lower()

            print(command)

    except:
        pass
    return command


def run_alexa():
    voice = take_command()
    if 'play' in voice:
        song = voice.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    if 'search' in voice:
        search = voice.replace('search', '')
        talk('searching'+search)
        pywhatkit.info(search, 3)
    if 'time' in voice:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('current time is'+time)


run_alexa()
