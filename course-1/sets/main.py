#Write a program to create a set and perform the following operations on that set- 
#1. Create a set with integer elements 
#2. Create a set with mixed data type elements 
#3. Create another set with elements - 1, 2, 3, 4, 3, 2 
#4. Create a set from a list with elements - [1, 2, 3, 2] 
#5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]
set1={1,2,3,4,5}
set2={1,"word",4.7,False}
set3={1,2,3,4,3,2}
set4=set([1,2,3,2])
set5={0,1,3,4,5}
set5.remove(0)
set_all=(set1,set2,set3,set4,set5)
print(set_all)