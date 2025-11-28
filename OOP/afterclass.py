#Write a program to create a dog class with one class variable and two instance variables, 
#and display the details of dogs of two different breeds.
class Dog:
    species="Golden Retriever"
    species1="German Shepherd"
    def __init__(self,name,age):
        self.name=name
        self.age=age    
dog1=Dog("Buddy",5)
dog2=Dog("Max",3)
print(f"{dog1.name} is a {dog1.species} and is {dog1.age} years old.")
print(f"{dog2.name} is a {dog2.species1} and is {dog2.age} years old.")