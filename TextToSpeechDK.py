# text to speech
#pip install pyttsx3
import pyttsx3 as pp
engine = pp.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[1].id)
speak = "Welcome to Natural Language programming"
engine.say(speak)
engine.save_to_file(speak, 'ab.mp3')
print("File Created Successfully ")
engine.runAndWait()
