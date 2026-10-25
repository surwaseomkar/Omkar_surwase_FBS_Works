# Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String

s="python is easy"

word=0
char=0

for ind in range(0,len(s)):
    if(s[ind]==" "):
        word=word+1
    else:
        char=char+1
    word=word+1

    print("Number of words=",word)
    print("Number of charcters=",char)