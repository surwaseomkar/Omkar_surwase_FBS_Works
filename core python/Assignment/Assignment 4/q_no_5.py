#WAP to print Fibonacci series upto n.

n=int(input('enter number:'))
a=0
b=1
for i in range(n):
 print(a)
 c=a+b
 a=b
 b=c