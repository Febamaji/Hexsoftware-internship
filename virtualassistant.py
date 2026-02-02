import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install sepech_recognition
import wikipedia
import webbrowser
import os

myName = 'Champaklal Jayanthilal Gada'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishme():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<=12:
        speak('Good morning, Kartik Aaryan')
    elif hour>12 and hour<18:
        speak('Good afternoon, Kartik Aaryan')
    else:
        speak('Good evening, Kartik Aaryan')
    speak(f'I am {myName}, How can I help you?')
    
def hearMe():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print('You said:', query)
    except Exception:
        print('Say that again, Please')
        return 'None'
    return query
    
    
if __name__=="__main__":
    wishme()
    while True:
        query = hearMe().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)
        elif 'open google' in query:
            webbrowser.open('www.google.com')
        elif 'open instagram' in query:
            webbrowser.open('www.instagram.com')
        elif 'coding asylum' in query:
            webbrowser.open('https://www.youtube.com/@codingasylum7377')
        elif 'play music' in query:
            music_dir = "C:\\Users\\Feba M Aji\\OneDrive\\Desktop\\Karaoke\\songs"
            songs = os.listdir(music_dir)
            speak('Playing Music...')
            song = os.path.join(music_dir, songs[2]) #os.startfile(path of the song)
            os.startfile(song)
        elif'code' in query:
            os.startfile("C:\\Users\\Feba M Aji\\OneDrive\\Desktop\\Hexsoftware internship\\fibonacci.py")
        elif'your pic' or 'your image' in query:
            os.startfile("C:\\Users\\Feba M Aji\\OneDrive\\Pictures\\Screenshots\\Screenshot 2026-02-03 022129.png")
        else:
            search = 'https://www.google.com/search?q='+query
            webbrowser.open(search)



