#Write a program to enter P, T, R and calculate Compound Interest

P=int(input("enter principal:"))
R=int(input("enter rate:"))
T=int(input("enter time:"))
amount=P*(1+R/100)**T
ci=amount-R
print("compound interest:",ci)