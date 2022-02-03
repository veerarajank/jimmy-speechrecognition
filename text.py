##text to speech configuration
import pyttsx3 as text
engine=text.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)
def texttospeech(audio):
    engine.say(audio)
    engine.runAndWait()