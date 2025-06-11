import webbrowser
import datetime
import Text_to_Speech
import Weather

def process(data):
    if data is None or data.strip() == "":
        return "I'm not able to understand."

    user_data = data.lower()

    if "what is your name" in user_data or "who are you" in user_data:
        response = "Hey, I'm Alex, your Virtual Assistant."
    elif "hello" in user_data or "hi" in user_data:
        response = "Hi Bhavisha, How can I help you?"
    elif "good morning" in user_data:
        response = "Good Morning Bhavisha"
    elif "good afternoon" in user_data:
        response = "Good Afternoon Bhavisha"
    elif "good evening" in user_data:
        response = "Good Evening Bhavisha"
    elif "good night" in user_data:
        response = "Good Night Bhavisha"
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        response = f"The current time is {current_time.hour} hour and {current_time.minute} minutes."
    elif "shutdown" in user_data:
        response = "Ok, Goodbye"
    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        response = "Spotify is ready for you"
    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        response = "Youtube is ready for you"
    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        response = "Google is ready for you"
    elif "weather" in user_data:
        response = Weather.weather()
    else:
        response = "I'm not able to understand"

    Text_to_Speech.Text_to_Speech(response)
    return response

