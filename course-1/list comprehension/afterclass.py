#Perform List Comprehension to get mentioned results.
num=[1,756,123,45,23,67,89,72,90]
even_num=[x for x in num if x%2==0]
print(even_num)
odd_num=[x for x in num if x%2!=0]
print(odd_num)
squared_num=[x**2 for x in num]
print(squared_num)
divide_num=[x/3 for x in num]
print([int(x) for x in divide_num])