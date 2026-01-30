#Write a program to create a class IOString which consists of a 
#constructor that gives a default value to variable str1.
#Next up create a method that gets a string as input from the user. 
#Create another method that will print the string in the upper case. 
#Next up create an object and call methods to get everything implemented.
class IOstring:
    def __init__(self):
        print("constructor initializer")
        self.string=""
    def get_string(self):
        self.string=input("Enter a string: ")
    def print_string(self):
        print(self.string)
obj=IOstring()
obj.get_string()
obj1=IOstring()
obj1.get_string()
obj.print_string()
obj1.print_string()