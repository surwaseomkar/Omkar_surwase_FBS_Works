# Python Program to Take in a String and Replace Every Blank Space
# with Hyphen

s="python is easy"
new=""
for ind in range(0,len(s)):
    if(s[ind]==" "):
        new=new+"-"
    else:
        new=new+s[ind]

print("original string=",s)
print("New string=",new)