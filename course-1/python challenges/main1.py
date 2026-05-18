#Write a Python Program to create a Guess the number game. 
#You can use different modules and functions to create this game. 
#Every time the user guesses wrong, drop a hint. You can drop additional hints as well.
import random
guess=False
pc=random.randint(1,20)
count=5
print("Welcome to the number guessing game!")
while count>0:
    uc=int(input("You need to guess a number between 1 and 20.\nWhat is your guess:\n------------------------------\n"))
    count-=1
    if uc>pc:
        print("Your guess is too high.")
    elif uc<pc:
        print("Your guess is too low.")
    else:
        print("Congratulations! You guessed it right.")
        guess=True
        break   
if not guess:
    print(f"Sorry, the number was {pc}. Better luck next time!")