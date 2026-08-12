# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)
import random
userid=input('enter userid:')
password=input('enter password:')
if userid=="omkar"  and   password=='1234':
    num=random.randint(0000,1111)
    print("captcha:",num)
    captcha=int(input('enter captcha:'))
    if num==captcha:
        print("login susscefully")
    else:
        print("captcha failed")
else:
    print("invalid userid and password:")
    