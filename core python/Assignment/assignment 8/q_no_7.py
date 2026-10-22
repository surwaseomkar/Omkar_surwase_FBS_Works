#Write a program to find sum of digits of a number.

def sum_digits(n):
    sum = 0

    while n> 0:
        digit = n % 10
        sum = sum +digit
        n = n // 10

    return sum
n =int(input("enter number:"))
result = sum_digits(n)
print("sum of digits =", result)