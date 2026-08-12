#Write a program to check if user has entered correct userid and password

userid=input("enter user id:")
password=input("enter password:")
if userid=="admin"  and   password=='1234':
    print("login succesfull")
else:
    print("invalid userid or password:")
