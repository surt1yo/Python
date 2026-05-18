#Write a program to create a class Vehicle and perform the following tasks - 
#1. Create an __init__ method with arguments - max_speed and mileage 
#2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 
#3. Print the values of max_speed and mileage by using the object
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
BMW=Vehicle(240,20)
Mercedes=Vehicle(200,25) 
print(f"The max speed of BMW is {BMW.max_speed}km/h and the mileage is {BMW.mileage}km/l")       
print(f"The max speed of Mercedes is {Mercedes.max_speed}km/h and the mileage is {Mercedes.mileage}km/l")       