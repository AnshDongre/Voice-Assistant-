import pyttsx3
import pywhatkit
import datetime



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
