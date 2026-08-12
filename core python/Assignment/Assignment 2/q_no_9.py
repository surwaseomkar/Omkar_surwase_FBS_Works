#Write a program to swap two numbers without using third variable

a=int(input('enter first number:'))
b=int(input('enter second number:'))
a=a+b
b=a-b
a=a-b
print(f'after swapping:first number{a} and {b}')