#Write a program to create a base class Bird, with a constructor and two methods. 
#Then, create a child class that inherits the constructor from Class Bird and has two functions. 
#Finally, display how you can use Super to access the parent class constructor inside the child class.
class Bird:
    def __init__(self):
        print("Bird is ready")
    def who_is_this(self):
        print("I am a bird")
    def swim1(self):
        print("I can swim")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def who_is_this(self):
        print("I am a penguin")
    def swim(self):
        print("I can swim")
obj=Penguin()
obj.who_is_this()
obj.swim()
obj.swim1()