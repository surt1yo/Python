"""
    To reinforce core concepts of Text-to-Speech (TTS), 
    user input handling, randomness, and command interpretation 
    by upgrading the original AI Voice Lab into a more interactive and responsive application.
                                                                                                """
import asyncio
import random
import pyttsx3
import speech_recognition as sr
from googletrans import Translator


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
        "1": "es",  # Spanish
        "2": "fr",  # French
        "3": "de",  # German
        "4": "zh-cn",  # Chinese (Simplified)
        "5": "ja"   # Japanese
    }
    print("Select a language to translate to:")
    for key, value in languages.items():
        print(f"{key}: {value}")
    choice = input("Enter the number corresponding to your choice: ")
    return languages.get(choice, None)

async def translate_text(text, target_language):
    translator = Translator()
    translation = await translator.translate(text, dest=target_language)
    return translation.text
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text
    
def speak(translated_text, target_language):
    engine = pyttsx3.init()
    engine.say(translated_text)
    engine.runAndWait()

if __name__ == "__main__":
    og_text = speech_to_text()
    target_language = language_selection()
    print(target_language)
    
    if og_text and target_language:
        translated_text = asyncio.run(translate_text(og_text, target_language))
        print(f"Translated text: {translated_text}")
        speak(translated_text,target_language)