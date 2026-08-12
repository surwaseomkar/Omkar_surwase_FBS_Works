#Write a program to check whether the triangle is equilateral, isosceles or scalene
# triangle

a=int(input('enter first angle:'))
b=int(input('enter second angle:'))
c=int(input('enter  second angle:'))
if a==b  ==c:
    print('equalienteral triangle:')
elif a==b or b==a or a==c:
    print('isosceles triangle:')
else:
    print('scalene triangle:')