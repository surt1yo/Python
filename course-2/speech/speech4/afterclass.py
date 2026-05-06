"""
    In this assignment, you will build a 
    complete console-based voice translation 
    application using speech recognition, 
    Google Translate, and text-to-speech. 
    The program takes spoken English input, 
    converts it to text, translates it into a 
    user-selected language, and then speaks the translated result.
                                                                    """
import pyttsx3
import speech_recognition as sr
from googletrans import Translator
from deep_translator import GoogleTranslator

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

def language_selection():
    languages = {
        "1": "es",
        "2": "fr",
        "3": "de",
        "4": "zh-CN",
        "5": "ja"
    }
    print("Select a language to translate to:")
    for key, value in languages.items():
        print(f"{key}: {value}")
    choice = input("Enter the number corresponding to your choice: ")
    return languages.get(choice)

def translate_text(text, target_language):
    translation = GoogleTranslator(source='auto', target=target_language).translate(text)
    print(f"Translated text: {translation}")
    return translation


def speak(translated_text, target_language):
    engine = pyttsx3.init()
    engine.say(translated_text)
    engine.runAndWait()

if __name__ == "__main__":
    og_text = speech_to_text()
    target_language = language_selection()
    print(target_language)

    if og_text and target_language:
        translated_text = translate_text(og_text, target_language)
        speak(translated_text, target_language)
