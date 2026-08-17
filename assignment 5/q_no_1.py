#1. Write a program to prompt user to enter userid and password. If Id and

id="omkar"
pas="1234"

for i in range(3):
    userid=input("Enter userid:")
    password=(input("Enter user password:"))
    if userid == id and password ==pas: 
        print("login succesfully")
        break
    else:
        print("Invalid user id and password")
else:
    print("complete 3 times program terminated")
