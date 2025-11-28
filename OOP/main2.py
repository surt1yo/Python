#Write a program to create a class Parrot and perform the following tasks - 
#1. Create a class variable species 
#2. Create a __init__ method that has instance variables - name and age 
#3. Create instances of class Parrot, passing arguments as well 
#4. Print Class variable by accessing it 
#5. Print Instance variables as well
class Parrot:
    species="Bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
parrot=Parrot("Harry",3)
parrot1=Parrot("Bob",4)
print(f"{parrot.name} is a {parrot.species} and is {parrot.age} years old.")
print(f"{parrot1.name} is a {parrot1.species} and is {parrot1.age} years old.")