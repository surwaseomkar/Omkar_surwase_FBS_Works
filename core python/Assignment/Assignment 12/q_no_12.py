# Python Program to count number of lowercase characters in a string.

s="python programming"
count=0

for ind in range(0,len(s)):
    if(s[ind]>='a' and s[ind]<='z'):
        count=count+1

print("Number of lowecase character=",count)