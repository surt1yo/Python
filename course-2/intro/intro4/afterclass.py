# Develop a Python-based Rock Paper Scissors game where 
# players compete against an AI opponent employing basic 
# strategies to enhance decision-making and programming skills.
import random
from colorama import Fore, Style, init
init(autoreset=True)
def get_ai_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(player_choice, ai_choice):
    if player_choice == ai_choice:
        return "tie"
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    if winning_combinations[player_choice] == ai_choice:
        return "player"
    else:
        return "ai"
def play_game():
    print(Fore.CYAN + "Welcome to Rock Paper Scissors!")
    while True:
        player_choice = input(Fore.YELLOW + "Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if player_choice == 'quit':
            print(Fore.MAGENTA + "Thanks for playing!")
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print(Fore.RED + "Invalid choice. Please try again.")
            continue
        ai_choice = get_ai_choice()
        result = determine_winner(player_choice, ai_choice)
        print(f"You chose: {Fore.GREEN}{player_choice}")
        print(f"AI chose: {Fore.BLUE}{ai_choice}")
        if result == "tie":
            print(Fore.YELLOW + "It's a tie!")
        elif result == "player":
            print(Fore.GREEN + "You win!")
        else:
            print(Fore.RED + "AI wins!")
        print()
if __name__ == "__main__":
    play_game()
