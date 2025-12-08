#Write a program to create a class Computer with a private attribute max_price 
#and methods sell(to display) the selling price and setmaxprice
#(change the private attribute max_price). 
#Now create an object for the class Computer.
#Try changing the value of max price and use the sell function to display the updated price. 
#Use a setter function to update the value and again display the price.
class Computer:
    __maxprice=900
    def sell(self):
        print("The maximum price is:", self.__maxprice)
    def setMaxPrice(self,price):
        self.__maxprice=price
obj=Computer()
obj.setMaxPrice(1000)
obj.sell()