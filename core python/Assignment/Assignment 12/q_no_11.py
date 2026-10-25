# Python Program to replace every blank space with hyphen in a string.

s="I am learning python"
new=""

for ind in range(0,len(s)):
    if(s[ind]==" "):
        new=new+"-"
    else:
        new=new+s[ind]

print("original string=",s)
print("New string",new)