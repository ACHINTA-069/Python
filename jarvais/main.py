import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary
import requests
import google.genai as genai

newsapi = "f735714a44604c9baf52d294ceebbee9"   # <-- replace with your valid API key

# Speak function with safe re-initialization
def speak(text):
    print(f"🗣 Speaking: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()





import google.genai as genai
from google.genai import types

# Initialize the client once globally
client = genai.Client(api_key="AIzaSyAn35IjK0ZDGYSGWIwRTPdTwOrVGW1R5aw")  # Replace with your key

def aiProcess(command):
    # Use the generate_content method for Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",  # or "gemini-1.5-flash"
        contents=command,
        config=types.GenerateContentConfig(
            system_instruction="You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."
        )
    )

    return response.text




# Command processor
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open github" in c.lower():
        webbrowser.open("https://github.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry Sir, I could not find that song in your library.")

    elif "news" in c.lower():
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=f735714a44604c9baf52d294ceebbee9"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if "articles" in data and len(data["articles"]) > 0:
                speak("Here are the top news headlines for today.")
                for i, article in enumerate(data["articles"][:5], start=1):
                    title = article.get("title")
                    if title:
                        print(f"{i}. {title}")   # print in terminal
                        speak(f"Headline {i}: {title}")
            else:
                speak("Sorry Sir, I could not find any news at the moment.")
        else:
            speak("Sorry Sir, I could not fetch the news right now.")

    else:
        #let open AI handle the request
        output = aiProcess(c)
        speak(output)

# Main program
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    r = sr.Recognizer()

    # List of possible wake words
    wake_words = ["jarvis", "java", "jarvise", "jarvas", "jarv"]

    while True:
        print("Listening for wake word 'Jarvis'...")

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=7, phrase_time_limit=8)

            word = r.recognize_google(audio)
            print(f"You said: {word}")

            # Check wake word
            if any(w in word.lower() for w in wake_words):
                speak("Yes Sir, I am listening for your command...")
                time.sleep(0.8)

                # Listen for the actual command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    print("🎤 Listening for command...")
                    audio = r.listen(source, timeout=7, phrase_time_limit=10)

                try:
                    command = r.recognize_google(audio)
                    print(f"✅ Command recognized: {command}")
                    processCommand(command)
                except sr.UnknownValueError:
                    print("⚠️ Could not understand the command.")
                    speak("Sorry Sir, I could not understand your command.")
                except sr.RequestError as e:
                    print(f"❌ Could not request results; {e}")

        except sr.UnknownValueError:
            print("⚠️ Could not understand the wake word.")
        except sr.RequestError as e:
            print(f"❌ Could not request results; {e}")
        except Exception as e:
            print(f"💥 Error: {e}")
