# Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary

s=input("Enter the string:")
dict={}
words=s.split()

for word in words:
    if(word in dict):
        dict[word]=dict[word]+1
    else:
        dict[word]=1

print("frequency of words=",dict)
