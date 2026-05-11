"""
    To reinforce how temperature settings 
    and instruction-based prompts influence 
    AI responses—helping students practice 
    generating structured, creative, and 
    tailored content using specific instructions 
    and temperature adjustments.
                                                """
                                                """
    In this interactive activity, 
    Students will experiment with 
    different temperature settings 
    to observe how they influence AI responses. 
    They will also learn to craft 
    instruction-based prompts to guide 
    AI outputs more effectively, 
    and explore the impact of context 
    and clarity on generated content.
                                                """
from colorama import Fore, Style
from hf import generate_resp
from groq import generate_response as generate_groq
import time
print("Welcome to ai engineering tutorial!")
temp = input("Enter a temperature setting (e.g., 0.3 for focused, 0.7 for creative): ")
try:
    temp = float(temp)
except ValueError:
    print("Invalid temperature. Using default of 0.3.")
    temp = 0.3
prompt = input("Enter an instruction-based prompt (e.g., 'Write a creative story about a dragon.'): ")


print("\nGenerating response with Hugging Face...")
print(Fore.RED + generate_resp(prompt, temperature=temp) + Style.RESET_ALL)


print("\nPART2: INSTRUCTION BASED PROMPTS")
topic = input("Enter a topic for the AI to write about (e.g., 'the future of AI'): ")
topic = input("Choose a topic (e.g., climate change, space exploration): ").strip()
prompts = [
        f"Summarize key facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if I'm a 10-year-old child.",
        f"Write a pro/con list about {topic}.",
        f"Create a fictional news headline from 2050 about {topic}.",
    ]
for i, p in enumerate(prompts,1):
    print(f"\nPrompt {i}: {p}")
    print(Fore.BLUE + generate_resp(p, temperature=temp) + Style.RESET_ALL)
    time.sleep(1)