# Python Program to Concatenate Two Dictionaries Into One

dict1={"a":10,"b":20}
dict2={"c":30,"d":40}

dict=dict1.copy()

for key in dict2:
    dict[key]=dict2[key]

print("dictionary 1=",dict1)
print("dictionary 2=",dict2)
print("new dictionary=",dict)