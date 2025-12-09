#Write a program to create a base class that consists of two functions - 
#one to display a value, and another function is an abstract method. 
#Next, create a subclass that consists of a method similar to the abstract method. 
#Finally, showcase how Abstraction is being implemented in this example.
from abc import ABC, abstractmethod
class hello(ABC):
    def display(self,value):
        print("The value is:", value)
    @abstractmethod
    def show(self):
        print("I am a abstract method.")
class hi(hello):
    def show(self):
        print("I am the show method inside the subclass.")   
obj=hi()           
obj.display(10)
obj.show()