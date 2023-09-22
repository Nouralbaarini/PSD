import math

a=int(input("Input number A "))
b=int(input("Input number B "))
c=int(input("Input number C "))
d=int(input("Input number D "))
e=int(input("Input number E "))


Add = (a+b+c+d+e)
print("Sum of all numbers is ",Add)

mean = (a+b+c+d+e)/5
print(f"The mean value is {mean}")

a1= (a - mean)**2
b2= (b - mean)**2
c3= (c - mean)**2
d4= (d - mean)**2
e5= (e - mean)**2

Sum = math.sqrt((a1 + b2 + c3 + d4 + e5)/5)

print(f"The standard deviation is {Sum} ")
