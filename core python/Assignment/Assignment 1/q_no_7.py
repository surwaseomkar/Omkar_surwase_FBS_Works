#Program to Find the Roots of a Quadratic Equation

import math
a=int(input("enter a value of a:"))
b=int(input("enter a value of b:"))
c=int(input("enter a value of c:"))
d=b*b-4*a*c
if d>0:
    root1=(-b + math.sqrt(d)) /(2*a)
    root2=(-b - math.sqrt(d)) /(2*a)
    print("root1=",root1)
    print("root=",root2)

else:
    print("imaganary root")
    