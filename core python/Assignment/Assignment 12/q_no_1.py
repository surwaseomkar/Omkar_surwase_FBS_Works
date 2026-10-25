# Python Program to Replace all Occurrences of ‘a’ with $ in a String

s="banana"
new=""

for ind in range(0,len(s)):
    if(s[ind]=='a'):
        new=new+"$"
    else:
        new=new+s[ind]

print("original string=",s)
print("New string=",new)