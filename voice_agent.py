import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

from agent.planner import plan
from agent.executor import check_scheme
from agent.checker import final_answer
import memory

import uuid
from gtts import gTTS
from playsound import playsound

def speak(text):
    filename = f"reply_{uuid.uuid4().hex}.mp3"
    tts = gTTS(text=text, lang="te")
    tts.save(filename)
    playsound(filename)



def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak in Telugu...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="te-IN")
        print("You said:", text)
        return text
    except:
        return ""


# ---- START AGENT ----

speak("నమస్కారం. నేను ప్రభుత్వ పథకాల సహాయకుడిని")

while True:
    user_text = listen()

    decision = plan(user_text, memory.memory)

    if decision == "ASK_AGE":
        speak("దయచేసి మీ వయస్సు చెప్పండి")
        age_text = listen()
        memory.save("age", 25)   # demo value
        continue

    if decision == "ASK_INCOME":
        speak("దయచేసి మీ ఆదాయం చెప్పండి")
        income_text = listen()
        memory.save("income", 150000)  # demo value
        continue

    if decision == "CHECK_SCHEME":
        result = check_scheme(memory.get("age"), memory.get("income"))
        response = final_answer(result)
        speak(response)
        break
