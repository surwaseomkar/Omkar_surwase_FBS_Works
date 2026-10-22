#Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n

def sum_series(n):
    sum = 0

    for i in range(1, n + 1):
        sum = sum + i

    return sum

n = int(input("enter n:"))
result = sum_series(n)
print("sum=",result)

# b. 1!+ 2! + 3! + 4!+..... + n!

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact *i

    return fact

def sum_factorial(n):
    sum=0

    for i in range(1, n + 1):
        sum = sum + factorial(i)

    return sum

n = int(input("enter n:"))
result = sum_factorial(n)
print("sum =",result)

# c. 1^1 + 2^2 + 3^3+ ...... n^n

def power_series(n):
    sum = 0

    for i in range(1, n + 1):
        sum = + i ** i

    return sum
n = int(input("enter n:"))
result = power_series(n)
print("sum =",result)
