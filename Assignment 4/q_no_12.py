#Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

num=int(input('enter the number:'))
count=len(str(num))
temp=num
arno=0
while num>0:
    d=num%10
    arno=arno+(d**count)
    num//=10
if temp==arno:
    print(f'{temp} number is armstrong')
else:
    print('number is not armstrong')