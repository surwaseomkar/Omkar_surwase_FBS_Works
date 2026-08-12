#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18

gender=input('enter gender:')
age=int(input('enter age:'))
if gender=="f":
    if age>18:
        print('female are eligible for marriage')
    else:
        print('female are not eligible for marriage')
else:
    if age>21:
        print('male are eligible for marriage')
    else:
        print('male are eligible for marriage')