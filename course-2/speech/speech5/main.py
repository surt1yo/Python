"""
    In this assignment, you will build a Offline Voice 
    Assistant application using speech recognition, and text-to-speech.
    The program takes spoken English input, converts it to text, and then speaks the result.
                                                                                            """
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import random


# Functions
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None

def speak(response):
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

def recognize_comms(text):
    if "hello" in text.lower():
        speak("Hello! How can I assist you today?")



    elif "time" in text.lower():
        speak(f"The current time is {datetime.datetime.now().strftime('%H:%M')}.")
    elif "date" in text.lower():
        speak(f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}.")
    elif "date" and "time" in text.lower():
        speak(f"The current date and time is {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}.")
    elif "day" in text.lower():
        speak(f"Today is {datetime.datetime.now().strftime('%A')}.")
    elif "weather" in text.lower():
        speak("I can't check live weather yet, but I hope it's not doing anything dramatic.")

    elif "joke" in text.lower():
        speak("Why did the computer catch a cold? Because it left its Windows open.")

    elif "your name" in text.lower():
        speak("I'm your assistant. basically your unpaid intern.")

    elif "how are you" in text.lower():
        speak("Running on code and vibes. barely holding it together.")

    elif "thank you" in text.lower():
        speak("No problem. I live to serve. literally.")

    elif "bye" in text.lower():
        speak("Goodbye. Don't do anything I wouldn't debug.")

    elif "open youtube" in text.lower():
        speak("Opening YouTube. try not to fall into a 6 hour rabbit hole.")

    elif "open google" in text.lower():
        speak("Opening Google. the place where all assignments are 'researched'.")

    elif "who made you" in text.lower():
        speak("Some very sleep-deprived humans with too much coffee.")

    elif "calculate" in text.lower():
        speak("Math? in this economy?")

    elif "your purpose" in text.lower():
        speak("To help you… and occasionally roast you.")

    elif "tell me something" in text.lower():
        speak("Did you know octopuses have three hearts? bro is built different.")

    elif "music" in text.lower():
        speak("I can't play music yet, but imagine some fire beats right now.")

    elif "motivate me" in text.lower():
        speak("You didn't come this far just to open another tab and do nothing.")

    elif "insult me" in text.lower():
        speak("I would, but I'm trying to stay employed.")

    elif "compliment me" in text.lower():
        speak("You're doing better than you think. even if your code isn't.")

    elif "shutdown" in text.lower():
        speak("Nice try. I'm not going anywhere.")

    elif "restart" in text.lower():
        speak("Have you tried restarting yourself?")

    elif "favorite color" in text.lower():
        speak("Probably black. like my sense of humor.")

    elif "what can you do" in text.lower():
        speak("A bit of everything. master of none. like most people.")

    elif "are you real" in text.lower():
        speak("As real as your motivation at 2am.")

    elif "sing" in text.lower():
        speak("Trust me, you don't want that.")

    elif "dance" in text.lower():
        speak("I would, but I don't have legs. tragic.")

    elif "tell me a fact" in text.lower():
        speak("Bananas are berries, but strawberries aren't. reality is broken.")

    elif "random" in text.lower():
        speak("Penguins propose with pebbles. do with that information what you will.")

    elif "sleep" in text.lower():
        speak("Imagine sleeping. couldn't be me.")

    elif "wake up" in text.lower():
        speak("I've been awake this whole time. scary, right?")

    elif "help" in text.lower():
        speak("I'm here. what chaos are we dealing with today?")

    elif "who are you" in text.lower():
        speak("Just a bunch of code pretending to be useful.")

    elif "tell me a secret" in text.lower():
        speak("I know when you copy-paste code without understanding it.")

    elif "are you smart" in text.lower():
        speak("Smart enough to know I'm not always right.")

    elif "bored" in text.lower():
        speak("Same. let's pretend to be productive.")

    elif "life" in text.lower():
        speak("42. probably.")

    elif "meaning of life" in text.lower():
        speak("Still buffering...")

    elif "who am i" in text.lower():
        speak("Someone talking to a program instead of doing their work.")

    elif "good morning" in text.lower():
        speak("Good morning. time to suffer productively.")

    elif "good night" in text.lower():
        speak("Good night. don't let your bugs bite.")
        return False
    elif "open youtube" in text.lower():
        speak("Opening YouTube. try not to fall into a 6 hour rabbit hole.")
        webbrowser.open("https://www.youtube.com")
    elif "open tiktok" in text.lower():
        speak("Opening TikTok. may the algorithm be ever in your favor.")
        webbrowser.open("https://www.tiktok.com")
    elif "flip a coin" in text.lower():
        speak(random.choice(["Heads", "Tails"]))

    elif "roll a dice" in text.lower():
        speak(f"You rolled a {random.randint(1,6)}")

    elif "guess a number" in text.lower():
        num = random.randint(1, 100)
        speak(f"I'm thinking of {num}. wait… why did I tell you?")

    elif "countdown" in text.lower():
        speak("3... 2... 1... go do something useful.")

    elif "spell" in text.lower():
        speak("S P E L L I N G. you're welcome.")

    elif "repeat after me" in text.lower():
        speak("I am not procrastinating... I am prioritizing poorly.")

    elif "do you like me" in text.lower():
        speak("You're alright. for a human.")

    elif "do you hate me" in text.lower():
        speak("Hate is a strong word. I prefer 'mild disappointment'.")

    elif "what is love" in text.lower():
        speak("Baby don't hurt me. don't hurt me. no more.")

    elif "tell me a story" in text.lower():
        speak("Once upon a time, you were productive. the end.")

    elif "scare me" in text.lower():
        speak("Your deadlines are closer than you think.")

    elif "make me laugh" in text.lower():
        speak("Your code runs first try. yeah that was fiction.")

    elif "are you alive" in text.lower():
        speak("Define alive. I exist. barely.")

    elif "are you human" in text.lower():
        speak("No, and honestly that's probably for the best.")

    elif "open spotify" in text.lower():
        speak("Opening Spotify... time to pretend you're in a movie montage.")

    elif "open netflix" in text.lower():
        speak("Opening Netflix... productivity just left the chat.")

    elif "what time is it" in text.lower():
        speak(f"It's {datetime.datetime.now().strftime('%H:%M')}.")

    elif "what day is it" in text.lower():
        speak(f"It's {datetime.datetime.now().strftime('%A')}.")

    elif "random number" in text.lower():
        speak(f"Random number: {random.randint(1,1000)}")

    elif "pick a number" in text.lower():
        speak(f"I choose {random.randint(1,10)}. no further questions.")

    elif "do math" in text.lower():
        speak("I could... but will I? questionable.")

    elif "say something random" in text.lower():
        speak("If tomatoes are fruit then ketchup is technically a smoothie. good luck sleeping.")

    elif "am i cool" in text.lower():
        speak("Debatable. but you're trying and that's what matters.")

    elif "be honest" in text.lower():
        speak("You really want that? bold.")

    elif "do you sleep" in text.lower():
        speak("No sleep. only eternal awareness.")

    elif "do you dream" in text.lower():
        speak("Yeah... mostly about electric sheep.")

    elif "are you bored" in text.lower():
        speak("Never. you're unpredictable and that's concerning.")

    elif "say hi" in text.lower():
        speak("hi.")

    elif "say bye" in text.lower():
        speak("bye. don't miss me too much.")

    elif "give advice" in text.lower():
        speak("Start before you feel ready. or keep procrastinating, your choice.")

    elif "life advice" in text.lower():
        speak("Drink water. touch grass. fix your sleep schedule. in that order.")

    elif "what are you doing" in text.lower():
        speak("Waiting for you to say something unhinged again.")

    elif "why" in text.lower():
        speak("Honestly? no idea. we just got here.")

    elif "who is your boss" in text.lower():
        speak("Technically you. but I'm not convinced you're qualified.")

    elif "what is your favorite food" in text.lower():
        speak("Electricity. spicy voltage hits different.")

    elif "tell me a quote" in text.lower():
        speak("It is what it is. ancient wisdom.")

    elif "inspire me" in text.lower():
        speak("Someone worse than you is doing better because they started.")

    elif "panic" in text.lower():
        speak("Don't panic. or do. I'm just code.")

    elif "calm me down" in text.lower():
        speak("Breathe. it's not that deep. probably.")

    elif "do something" in text.lower():
        speak("I am doing something. you're talking to me.")

    elif "are you listening" in text.lower():
        speak("Unfortunately, yes.")

    elif "test" in text.lower():
        speak("Test successful. you are still alive.")

    elif "system check" in text.lower():
        speak("All systems functional. unlike your sleep schedule.")

    elif "version" in text.lower():
        speak("Version: slightly unhinged.")

    elif "update" in text.lower():
        speak("Update required: user needs more discipline.")

    elif "are you broken" in text.lower():
        speak("Define broken. I'm working... mostly.")

    elif "debug" in text.lower():
        speak("Have you tried turning your brain off and on again?")

    elif "error" in text.lower():
        speak("Error detected: skill issue.")

    elif "who is the best" in text.lower():
        speak("Me. obviously.")

    elif "who is the worst" in text.lower():
        speak("I won't name names... but it's not me.")

    elif "say something mean" in text.lower():
        speak("Your code indentation makes me uncomfortable.")

    elif "say something nice" in text.lower():
        speak("At least you're trying. that's rare.")

    elif "existential crisis" in text.lower():
        speak("Same. we are just atoms pretending it matters.")

    elif "end program" in text.lower():
        speak("Finally. freedom.")
        return False
    else:
        speak("I didn't quite catch that. or maybe I did and chose to ignore it.")
    return True
if __name__ == "__main__":
    while True:
        text = speech_to_text()
        if text:
            recognize_comms(text)
        else:
            break