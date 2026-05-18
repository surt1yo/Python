#Write a program to implement abstraction on animal class (base class). 
#The abstract method will be move will display what subclasses can do. 
#Subclasses can be something like - Human, Dog.
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        print("Animals make different sounds.")
class Dog(Animal):
    def sound(self):
        print("Dogs bark.")
class Human(Animal):
    def sound(self):
        print("Humans speak.")
obj=Dog()
obj.sound()
obj1=Human()
obj1.sound()