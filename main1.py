#Write a program to check whether the given tuple -
#(1,2,3,3,2,1) is a palindrome or not. 
#If it's a palindrome, then it is the same after being reversed.
tuple=(1,2,3,3,2,1)
reversed_tuple=tuple[::-1]
print(reversed_tuple)
if tuple==reversed_tuple:
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")