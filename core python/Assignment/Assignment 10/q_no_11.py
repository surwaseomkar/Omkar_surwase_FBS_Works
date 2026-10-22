# Write a program to print all numbers which are divisible by m and n in the list.

li=[10 ,20, 30, 40, 50, 60, 70, 80, 90, 100]

m=2
n=5

for ind in range (0, len(li)):
    if(li[ind]%m==0 and li[ind]%n==0):
        print(li[ind])
