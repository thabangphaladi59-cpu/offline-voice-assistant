# Offline Voice Assistant - by Thabang Phaladi
# Works 100% offline on Dell D630
import pyttsx3
import datetime
import os

engine = pyttsx3.init()
engine.setProperty('rate', 180)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M")

def main():
    speak("Hello Thabang. Offline assistant ready on D630.")
    print("Type 'exit' to quit. Commands: time, date, open folder, hello")
    
    while True:
        command = input("\nYou: ").lower()
        
        if "time" in command:
            speak(f"The time is {get_time()}")
        elif "date" in command:
            today = datetime.date.today()
            speak(f"Today is {today}")
        elif "open" in command and "folder" in command:
            speak("Opening documents folder")
            os.startfile(os.path.expanduser("~\\Documents"))
        elif "hello" in command or "hi" in command:
            speak("Hello! How can I help you offline?")
        elif "exit" in command or "bye" in command:
            speak("Goodbye Thabang. Shutting down.")
            break
        else:
            speak("I heard you, but I'm still learning that command. Try saying time.")

if __name__ == "__main__":
    main()
