# Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n -1)

def sum_fac(n):
    if n == 0:
        return 0
    return fact(n) + sum_fac(n -1)

n = int(input("enter n:"))
print("sum =", sum_fac(n))



    
