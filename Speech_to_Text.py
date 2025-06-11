import speech_recognition as sr

def Speech_to_Text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
            return voice_data
        except sr.UnknownValueError:
            return "I didn't catch that. Could you please repeat?"
        except sr.RequestError:
            return "Sorry, my speech service is down."
