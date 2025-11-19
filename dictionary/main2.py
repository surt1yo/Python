#Write a program to return the country code for various countries.
#Here’s a dictionary of different country codes - 
#{'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.
codes={'India':'0091','Australia':'0025','Nepal':'00977'}
print(codes['Nepal'])
print(codes.get('Japan','Not Found'))
codes1=codes.copy()
codes.clear()
print(codes)
print(codes1)