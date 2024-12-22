#Farenheit to celsius
""" f=int(input())
c=(f-32)*5/9
print(c) """

#swap two numbers
""" a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(a,b) """

#checking the dictionary
d={1:"a",2:"b",3:"c"}
k=input("Enter any key to find out:")
if k in d.values():
    print("Key found")
else :
    print("Not found")