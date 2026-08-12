#WAP to check the number is pallindrome or not
# return True if pallindrome & return False if not pallindrome

def chkpallindrome(num):
    temp = num
    rev = 0
    while(temp >0):
        d = temp % 10
        temp = temp //10
        rev = rev* 10+d
    if(num ==rev):
        return True
    else:
        return False

n = int(input('enter number:'))
print(chkpallindrome(n))