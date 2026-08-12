#Write a program to input all sides of a triangle and check whether triangle is valid or not

a=int(input('enter first angle:'))
b=int(input('enter second angle:'))
c=int(input('enter  second angle:'))
if(a+b>c) and (a+c>b)  and (b+c>a):
    print("triangle is valid")
else:
    print("triangle is not valid")
