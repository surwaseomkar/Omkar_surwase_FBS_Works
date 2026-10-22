#Write a program to find sum of digits using recursion.

def sum_digits(n):
    if n ==0:
        return 0
    return (n % 10) + sum_digits(n // 10)

num =int(input("Enter number:"))
print("sum of digits=", sum_digits(num))

