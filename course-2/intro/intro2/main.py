# In this activity, you will interact with an 
# AI-powered "Sentiment Spy" chatbot, which 
# uses Textblob a natural language processing 
# Library to analyze the emotions in their text 
# messages (positive, neutral, or negative). 
# You will explore how AI detects sentiment in 
# real time and receive mission-themed feedback,
#  making learning fun and engaging!
import colorama
from colorama import Fore, Style
from textblob import TextBlob
# Initialize colorama for colored text output
colorama.init()
print(f"{Fore.GREEN}Welcome to the Sentiment Spy Mission!{Style.RESET_ALL}")
name = input(f"{Fore.YELLOW}What is your name? {Style.RESET_ALL}")
if not name or name.isdigit():
    name = "Agent X"
print(f"{Fore.CYAN}Hello, {name}!{Style.RESET_ALL}")    
convo_hist = []
while True:
    user_input = input(f"{Fore.GREEN}>> Enter a text to analyze the sentiment or type 'exit' to end the mission: {Style.RESET_ALL}").strip()
    if not user_input:
        print("Please enter valid text.")
        continue
    elif user_input.lower() == 'exit':
        print(f"{Fore.BLUE}Mission abandoned, Goodbye, {name}!{Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        convo_hist.clear()
        print(f"{Fore.CYAN}Conversation history has been reset.{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not convo_hist:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.MAGENTA}Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment) in enumerate(convo_hist, 1):
                if sentiment == "Positive":
                    color = Fore.GREEN
                elif sentiment == "Negative":
                    color = Fore.RED
                else:
                    color = Fore.YELLOW
                
                print(f"{color}{idx}. {text} - Polarity: {polarity:.2f}, Sentiment: {sentiment}{Style.RESET_ALL}")
            continue
    # Analyze the sentiment of the user input
    blob = TextBlob(user_input).sentiment.polarity
    if blob > 0.25:
        sentiment = "positive"
        color = Fore.GREEN
    elif blob < -0.25:
        sentiment = "negative"
        color = Fore.RED
    else: 
        sentiment = "neutral"
        color = Fore.YELLOW
    convo_hist.append((user_input, blob, sentiment))
    print(f"{color}Sentiment: {sentiment}{Style.RESET_ALL}")