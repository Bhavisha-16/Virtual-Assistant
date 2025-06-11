import pyttsx3

def Text_to_Speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)  # Correct rate adjustment
    engine.say(text)
    engine.runAndWait()
