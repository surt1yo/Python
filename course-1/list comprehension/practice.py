num=[1,756,123,45,23,67,89,72,90]
even_num=[x for x in num if x%2==0]
print(even_num)
num1=[54,76,451,68,923,54,47,32,64]
num2=[526,34,12,89,45,23,67,89,90]
num3=map(lambda x,y:x+y,num1,num2)
print(list(num3))