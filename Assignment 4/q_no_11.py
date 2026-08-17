#WAP to check if given number Strong Number.

num=int(input('enter number:'))
temp=num
sum=0
while num>0:
    d=num% 10
    fact=1
    for i in range(1,d+1):
        fact=fact*i
    sum=sum+fact
    num=num//10

if sum==temp:
    print('strong number')
else:
    print('not strong number')
    