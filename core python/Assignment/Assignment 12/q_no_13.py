# Python Program to count number of digits and letters in a string.

s="python123"

digit=0
letter=0

for ind in range(0,len(s)):
    if(s[ind]>='0' and s[ind]<='9'):
        digit=digit+1
    elif(s[ind]>='a' and s[ind]<='z'):
             letter=letter+1

print("Number of digits=",digit)
print("Number of lettters=",letter)