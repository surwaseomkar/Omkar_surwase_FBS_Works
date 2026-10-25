# Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).

n=int(input("Enter the value of n:"))
dict={}

for x in range(1,n+1):
    dict[x]=x*x

print("Dictionary=",dict)