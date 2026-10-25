# Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

s="python is easy python is simple"

words=s.split()

unique=set(words)

print("String=",s)
print("Unique words=",unique)

for word in unique:
    print(word,"=",words.count(word))