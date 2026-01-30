#Write a Python program to create a class that will find the numbers 
#in the tuple that add up to a sum and return the position of elements. 
#The value of the sum can be taken as input from the user. 
#Tuple - (10,20,30,40,50,60,70)

class FindPair:
    def __init__(self,tuple,num):
        self.tuple=tuple
        self.num=num       
    def findthepair(self):
       for i,n in enumerate(self.tuple):
           if self.num-n in self.tuple:
              return (self.tuple.index(self.num-n),i)
                       
t_input=int(input("Enter the sum of which you want to find the pair of elements: "))
tuple=(10,20,30,40,50,60,70)

obj=FindPair(tuple,t_input)
x,y=obj.findthepair()
print(f"The pair of elements that add up to {t_input} are at positions: {x} and {y}.")


