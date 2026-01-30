#Write a program to create an array with the following elements - 
#[1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array.
#Also, print the reversed array.
import array as arr
array1=arr.array('i',[1,3,5,3,7,9,3])
array2=arr.array('d',[1,3,5.6,3,7,9,3])
print(array1)
print(array2)
count=array1.count(3)
print(count)
array1.reverse()
print(array1)
print(array2[2])

