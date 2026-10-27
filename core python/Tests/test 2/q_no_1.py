# Write a program to accept year from user and check if it is a leap year or not.



year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap year")

elif year % 100 == 0:
    print("Not a leap year")

elif year % 4  == 0:
    print("Leap year")
else:
    print("Not a Leap year2026")