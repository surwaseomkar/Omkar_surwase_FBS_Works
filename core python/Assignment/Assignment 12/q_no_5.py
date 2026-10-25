# Python Program to Count the Number of Vowels in a String
s="education"
count=0

for ind in range(0,len(s)):
    if(s[ind] in "aeiouAEIOu"):
        count=count+1

print("Number of vowels=",count)
