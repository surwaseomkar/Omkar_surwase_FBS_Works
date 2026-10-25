# Python Program to Multiply All the Items in a Dictionary

dict={"a":10,"b":20,"c":30}

mul=1

for key in dict:
    mul=mul*dict[key]

print("Dicyionary=",dict)
print("Milriplication of all items=",mul)