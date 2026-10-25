# Python Program to count the occurrences of each word in a string.

s="python is easy python is good"

words=s.split()

for i in range(0,len(words)):
    count=0

    for j in range(0,len(words)):
        if(words[i]==words[j]):
            count=count+1

print(words[i],"=",count)