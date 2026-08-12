#Write a program to convert days into years, weeks and days

d=int(input("enter total days:"))
year=d//365
d=d%365
days=d//365
d=d%365
week=d//7
d=d%7
print(f' year{year},days{days},week{week}:')