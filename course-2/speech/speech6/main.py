""""
    Speech Translator with Text-to-Speech" 
    is an interactive application that allows
    users to speak a sentence in English. 
    The application then translates the spoken 
    sentence into a selected language, and the 
    translated text is spoken back to the user. 
    This activity uses Speech Recognition to 
    convert speech to text, Google Translate API 
    to translate the text into the selected language, 
    and Text-to-Speech to speak the translated text aloud. 
    It supports multiple languages for translation 
    and can help users learn basic translation 
    and language conversion in a hands-on, interactive manner.
                                                                """
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import random
import os
from googletrans import Translator
from gtts import gTTS
import platform

translator = Translator()

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

def speak(response, language="en"):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if language == "en":
        engine.setProperty('voice', voices[0].id)  # English voice
    else:
        engine.setProperty('voice', voices[1].id)
    engine.say(response)
    engine.runAndWait()

def speak1(response,language="en"):
    tts = gTTS(text=response, lang=language)
    filename = "output.mp3"
    tts.save(filename)

    # Play audio based on OS
    if platform.system() == "Windows":
        os.system(f"start {filename}")
    

def display_language():
    languages = {
        "1": "es",
        "2": "fr",
        "3": "de",
        "4": "zh-cn",
        "5": "ja",
        "6": "tl"
    }
    print("Select a language to translate to:")
    for key, value in languages.items():
        print(f"{key}. {value}")
    choice = input("Enter the number corresponding to the language: ")
    return languages.get(choice, None)

def translate_text(text, target_language):
    result = translator.translate(text, dest=target_language)
    print(f"Translated text: {result.text}")
    if result.text:
        speak1(result.text, language=target_language)
    return None

if __name__ == "__main__":
    while True:
        text = speech_to_text()
        target_language = display_language()
        if text and target_language:
            translate = translate_text(text, target_language)