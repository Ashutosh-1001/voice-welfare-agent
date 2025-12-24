import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak in Telugu...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language="te-IN")
    print("You said:", text)
except:
    print("Sorry, I did not understand")
