#Find the sum of three-digit number. 

num=int(input('enter three digit number:'))
d1=num%10
num=d1//10
d2=num%10
num=d2//10
d3=num%10
num=d3//10
sum_of_digit=d1+d2+d3
print('the sum of digit is',sum_of_digit)