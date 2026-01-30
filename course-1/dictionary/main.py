#First, create a dictionary that consists of - id, name, class and subject integration of students. 
#Then, write a program to retrieve unique entries and eliminate the rest.
me={
    "S1332582":{"NAME":"mezaan","class":"6","subjects":["maths","science","literacy","reading"]},
    "S1332583":{"NAME":"ahmed","class":"6","subjects":["maths","science","literacy","reading"]}
}
for key,value in me.items():
    print(f"ID: {key}:{value}")