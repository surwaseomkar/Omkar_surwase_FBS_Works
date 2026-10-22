#Write a program to check if entered number is a palindrome or not.

def reverse_number(n):
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

n = int(input("enter number:"))
reverse= reverse_number(n)
if n == reverse:
    print("pallindrome number")
else:
    print("not a pallindrome number")