#Write a program to check if entered year is a leap year or not.

def check_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 !=0:
        return True
    else:
        return False

year = int(input("enter year:"))
if check_leap_year(year):
    print("leap year")
else:
    print("not a leap year")