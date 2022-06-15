#pip install SpeechRecognition
#pip install pyaudio
import  speech_recognition as sr
r = sr.Recognizer()
while True:
    try:
        with sr.Microphone() as  mic:
            r.adjust_for_ambient_noise(mic, duration=1)
            print("Please speak something")
            audio = r.listen(mic)

            text = r.recognize_google(audio)
            test = text.lower()
            print(text)
            break
    except:
        break
