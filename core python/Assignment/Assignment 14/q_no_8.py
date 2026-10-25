# Write a Python program to find all the anagrams and group them
# together from a given list of strings.

words=["eat","tea","tan","ate","nat","bat"]
dict={}

for word in words:
    key="".join(sorted(word))
    if(key in dict):
        dict[key]=[word]
    else:
        dict[key]=[word]

print("Angrams=",dict)
