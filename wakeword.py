import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                return command
    except:
        pass
    return command



def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I am not interested')
    elif 'are you free now' in command:
        talk('Nope I am busy coding')
    elif 'are you single' in command:
        talk("I am in relationship with wifi")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open facebook' in command:
        talk('opening facebook')
        webbrowser.open('https://www.facebook.com')
    elif 'yourself' in command:
        talk('Okay,I am Alexa,I am your digital assistant')
    else:
        talk('Please say the command again')



while True:
    run_alexa()
