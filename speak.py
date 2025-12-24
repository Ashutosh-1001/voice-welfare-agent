import uuid
from gtts import gTTS
from playsound import playsound

def speak(text):
    filename = f"reply_{uuid.uuid4().hex}.mp3"
    tts = gTTS(text=text, lang="te")
    tts.save(filename)
    playsound(filename)
