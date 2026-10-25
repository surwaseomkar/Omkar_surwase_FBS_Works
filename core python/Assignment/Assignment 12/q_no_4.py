# Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

s="python"
new=s[len(s)-1]

for ind in range(1,len(s)-1):
    new=new+s[ind]

new=new+s[0]

print("original string=",s)
print("New string=",new)