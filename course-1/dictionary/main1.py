#Write a program to check the frequency of a value in a dictionary -
#{'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.
dictionary={"Codingal":2,"is":2,"best":2,"for":2,"Coding":1}
count=0
for key,value in dictionary.items():
    if dictionary[key]==2:
        count+=1
print(f"There is {count} values with the frequency of 2.")