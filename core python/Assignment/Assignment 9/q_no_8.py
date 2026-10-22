#Write a program to check whether a number is prime or not using recursion.

def prime(n, divisor):
    if n < 2:
        return False

    if divisor *divisor > n:
        return True

    if n % divisor == 0:
        return False

    return prime(n, divisor + 1)

num = int(input(" Enetr number:"))
if prime(num, 2):
    print("primr number")
else:
    print("Not prime number")