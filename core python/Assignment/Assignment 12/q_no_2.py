# Python Program to Remove the nth Index Character from a Non-Empty
# String

s="python"
n=2
new=""

for ind in range(0,len(s)):
    if(ind!=n):
        new=new+s[ind]

print("original string=",s)
print("New string=",new)
