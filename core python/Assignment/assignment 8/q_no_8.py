#Write a program find reverse of a number

def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    return rev
n = int(input("enter number:"))
result = reverse_number(n)
print("reverse =", result)