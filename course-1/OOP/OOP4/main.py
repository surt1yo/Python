#Write a program to create a class with following variables and methods - 
#1. Private variable named privateVar that contains an integer value 
#2. Create a private function privMeth that prints a message 
#3. Create a function hello that prints the value of private Var 
#4. Create an object for the class and call all the functions.
class MyClass:
    __privateVar=42
    def __privMeth(self):
        print("The value of privateVar is:", self.__privateVar)
    def display(self):
       self.__privateVar=100
       print(self.__privateVar)

obj=MyClass()
obj.display()
    