#Write a program to overload the less than (<) and equal to (==) operators. 
#For example, create objects - ob1 and ob2 with values 3 and 4 to compare values,
#respectively. You can additionally create more objects to try different values.
class Number:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        if self.value < other.value:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.value == other.value:
            return True
        else:    
            return False   
    def __add__(self, other):
        return self.value + other.value    
obj=Number(5) 
obj1=Number(7)
print(obj+obj1)        
if obj < obj1:
    print(f"{obj.value} is less than {obj1.value}.")
elif obj == obj1:
    print(f"{obj.value} is equal to {obj1.value}.")    
else:
    print(f"{obj.value} is greater than {obj1.value}.")    