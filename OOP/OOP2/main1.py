#Write a program to create a class with the named employee and create a constructor and destructor. 
#Then, write a function to create an object for that class and delete the object. 
#Make sure you call the function to get everything implemented!
class employee:
    def __init__(self):
        print("Construtor initialized")  
    def __del__(self):
        print("Destructor called, employee object deleted.")
print("Creating employee object...")   
e1=employee()
print("Job of employee done.")