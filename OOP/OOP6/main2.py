#Write a program to create a quiz related to multiple fruits using 
#object-oriented programming in Python. Create a class that consists of 
#- 1. a constructor with a dictionary of fruits and respective colours 
#2. a function to execute the quiz. Here, the fruit will be chosen at random from the dictionary. 
#Then ask the user to enter the colour of that fruit. 
#Evaluate the answer and display the result accordingly
import random
class Fruit:
    def __init__(self):
        self.fruits_dict={
            "Apple":"Red",
            "Banana":"Yellow",
            "Grapes":"Purple",
            "Orange":"Orange",
            "Kiwi":"Brown",
            "Mango":"Yellow",
            "Blueberry":"Blue",
            "Lemon":"Yellow",
            "Strawberry":"Red",
            "Watermelon":"Green"
        }
    def execute_quiz(self):
        for fruit,colour in self.fruits_dict.items():
            print(f"What is the colour of {fruit}?")      
            answer=input("Your answer: ")
            if answer.lower()==colour.lower():
                print("Correct!\n--------------------------------")
            else:
                print(f"Incorrect! The correct colour is {colour}.\n--------------------------------")
fruit=Fruit()
fruit.execute_quiz()                