# Python Program to Detect if Two Strings are Anagrams
s1="listen"
s2="silent"

s1=sorted(s1)
s2=sorted(s2)

if(s1==s2):
    print("string are anagrams")
else:
    print("string are not anagrams")
    