#WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

def check_armstrong(n):
    original = n
    digits = len(str(n))
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + digit ** digits
        n = n //10

    if sum == original:
        return True
    else:
        return False

n = int(input("enter number:"))
if check_armstrong(n):
    print("armstrong number")
else:
    print("not an armstrong number")