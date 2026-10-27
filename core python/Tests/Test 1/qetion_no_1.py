#Write a program to find the area and perimeter of following figure (Accept the 
# length, breadth and radius from user

import math
length = int(input("Enter length:"))
breadth =int(input("Enter breadth:"))
radius =int(input("Enter radius:"))

area = (length*breadth) + (math.pi*radius*radius/2)
perimeter = (2*length) + breadth + (math.pi*radius)

print("Area =",area)
print("perimeter =",perimeter)