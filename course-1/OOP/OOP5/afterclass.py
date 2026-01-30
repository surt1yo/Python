#Write a Python program to create two classes - 
#BMW and Ferrari with similar methods and implement 
#polymorphismPolymorphism on them.
class BMW:
    def origin(self):
        print("BMW is a German car manufacturer.")
    def maxspeed(self):
        print("The maximum speed of BMW cars is around 300 k/h.")
    def price(self):
        print("The average price of a BMW is around $100,000.\n--------------------------------")
class Ferrari:
    def origin(self):
        print("Ferrari is an Italian car manufacturer.")
    def maxspeed(self):
        print("The maximum speed of Ferrari cars is around 340 k/h.")
    def price(self):
        print("The average price of a Ferrari is around $250,000.")
bmw = BMW()
ferrari = Ferrari()
for car in (bmw,ferrari):
    car.origin()
    car.maxspeed()
    car.price()
    