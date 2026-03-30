# In this hands-on activity, you'll build and explore 
# an interactive command-line tool that leverages the 
# Hugging Face API for text summarization. Participants 
# will learn how to send HTTP requests, handle JSON 
# responses, and customize summarization parameters such 
# as minimum and maximum summary lengths. The tool also 
# demonstrates integrating colorful terminal outputs using 
# Colorama for enhanced user interaction. By the end of 
# this exercise, you'll have a deeper understanding of how 
# to build AI-powered applications that can transform large 
# blocks of text into concise summaries, making it a practical 
# introduction to working with modern AI APIs.
import requests
from colorama import Fore, Style
from conflg import hf_api_key

# Api key
base_url = "https://router.huggingface.co/hf-inference/models"
model = "facebook/bart-large-cnn"
api_url = base_url + "/" + model

# Functions
if __name__ == "__main__":
    print(Fore.GREEN + "Welcome to the Text Summarization Tool!" + Style.RESET_ALL)
    name = input("Please enter your name: ")
    if name == "":
        pass
    else:
        print(Fore.BLUE + f"Hello, {name}! Let's get started with summarizing your text." + Style.RESET_ALL)
    text = input(Fore.YELLOW + "\nPlease enter the text you want to summarize (press Enter twice to finish):" + Style.RESET_ALL)
    if text == "":
        print(Fore.RED + "No text entered. Exiting the program." + Style.RESET_ALL)
        exit()
    else:
        print(Fore.GREEN + "\nYou entered the following text:\n" + Style.RESET_ALL + text)
        summary = input(Fore.BLUE + "\nDo you want a short or long summary? (Enter 'short' or 'long'): " + Style.RESET_ALL)
        if summary != "short" and summary != "long":
            print(Fore.RED + "Invalid input. Please enter 'short' or 'long'." + Style.RESET_ALL)
            print(summary)
            exit()
        elif summary.lower() == "short":
            min_length = 20
            max_length = 50
        elif summary.lower() == "long":
            min_length = 50
            max_length = 100

        print(Fore.CYAN + "\nSummarizing your text..." + Style.RESET_ALL)
        headers = {
            "Authorization": f"Bearer {hf_api_key}"
        }
        payload = {
            "inputs": text,
            "parameters": {
                "min_length": min_length,
                "max_length": max_length
            }
        }
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=30)
            if response.status_code != 200:
                print(Fore.RED + f"Error: {response.status_code} - {response.text}" + Style.RESET_ALL)
            else:
                summary_result = response.json()[0]["summary_text"]
            print(Fore.GREEN + f"\nHere is your summary:\n{summary_result}" + Style.RESET_ALL)
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"❌ API Request Failed: {e}")
            
        

