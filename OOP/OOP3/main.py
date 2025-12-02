#Write a Python program to implement Inheritance by creating a Parent Class 
#Vehicle with a constructor that has details like name, maximum speed, and mileage. 
#Then, create a Child Class Bus that inherits Class Vehicle. 
#Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.
class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(Vehicle):
    pass
    #def __init__(self,name,max_speed,mileage):
        #super().__init__(name,max_speed,mileage)
        #print(f"Vehicle Name: {self.name}, Maximum Speed: {self.max_speed} km/h, Mileage: {self.mileage} km/l")
obj=Bus("School Volvo",180,12)
print(f"Vehicle Name: {obj.name}, Maximum Speed: {obj.max_speed} km/h, Mileage: {obj.mileage} km/l")
