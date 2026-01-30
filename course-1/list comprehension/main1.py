#Write a program to return - 
#1. zipped list from two lists
#2. elements of two lists zipped together, but 2nd list in reverse order 
#3. elements of two lists zipped into a dictionary
list1=["mezaan","dean","james","mason"]
list2=[11,10,12,11]
zip_list=list(zip(list1,list2))
print(zip_list)
reversed_list=list(zip(list1,(list2[::-1])))
print(reversed_list)
dict={x:y for x,y in zip(list1,list2)}
for key,value in dict.items():
    print(f"{key}:{value}")