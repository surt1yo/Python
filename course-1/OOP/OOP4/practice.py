#Write a Python program to create a class that represents a shape. 
#Include methods to calculate its area and perimeter. 
#Implement subclasses for different shapes like circle, triangle, and square.
import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("The area of the circle is:",math.pi*self.radius**2)
    def perimeter(self):
        print("The peremiter of the circle is:",2*math.pi*self.radius)
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print("The area of the square is:",self.side**2)
    def perimeter(self):
        print("The perimeter of the square is:",4*self.side)
obj=Circle(5)
obj.area()
obj.perimeter()
obj1=Square(4)
obj1.area()
obj1.perimeter()