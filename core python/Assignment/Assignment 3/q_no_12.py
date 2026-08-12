#write a program to check if given 3 digit number is a palindrome or not

num=int(input('enter three digit number:'))

temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10
if num==rev:
    print("palindrome")
else:
    print("not palindrome")