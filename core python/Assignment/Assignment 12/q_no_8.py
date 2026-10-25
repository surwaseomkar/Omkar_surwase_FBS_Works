# Python Program to Remove the Characters of Odd Index Values in a
# String

s="python"
new=""
for ind in range(0,len(s)):
    if(ind%2==0):
        new=new+s[ind]

print("original string=",s)
print("New string=",new)