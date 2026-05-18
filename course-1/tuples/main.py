#Write a program to perform the following operations: 
#1. Create a tuple with different datatypes 
#2. Create another tuple of integers 
#3. Create a new tuple by adding 9 to the previous tuple 
#4. Count the occurrences of an element in the tuple 
#5. Perform slicing on the tuple
tuple=("Hello", 42, 3.14, True)
print(tuple)
tuple1=(1,2,3,4,5)
print(tuple1)
tuple2=tuple1+(9,)
print(tuple2)
tuple3=(1,1,2,2,3,3,4,4)
print(tuple3.count(2))
print(tuple3[3:6])
