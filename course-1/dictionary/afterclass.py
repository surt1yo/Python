#Check the frequency of a value in the given test dictionary.
dictionary={"Codingal":3,"is":2,"best":2,"for":2,"Coding":1}
input_value=input("Enter the value to check its frequency: ")
count=0
for key,value in dictionary.items():
    if dictionary[key]==int(input_value):
        count+=1
print(f"Frequency of the value {input_value} is: {count}.")