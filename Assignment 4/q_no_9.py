#WAP to print all numbers in a range divisible by a given number.

num=int(input('enter number:'))
d=int(input('enter number:'))
for i in range(1,num+1):
    if i % d==0:
        print(i)