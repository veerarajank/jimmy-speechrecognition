##speech to text configuration
import speech_recognition as speak 
def speechtotext(timeout):
    recog=speak.Recognizer()
    with speak.Microphone() as source:
        try:
            audio=recog.listen(source,timeout)
            query=recog.recognize_google(audio)
            return query
        except:
            return "Timeout"
        