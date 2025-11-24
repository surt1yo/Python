#Write a program to return the addition of numbers of two different lists. 
#Then, display a list that is square of numbers of another list.
#Use the map() function here to get the desired result.
num=[1,756,123,45,23,67,89,72,90]
num1=[54,76,451,68,923,54,47,32,64]
add_num=map(lambda x,y:x+y,num,num1)
print(list(add_num))

num3=[1,2,3,4,5,6,7,8,9]
squared_num=list(map(lambda x:x**2,num3))
print(squared_num)