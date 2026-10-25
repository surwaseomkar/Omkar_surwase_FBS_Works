# Python Program to Sum All the Items in a Dictionary

dict={"a": 10,"b":20,"c":30}
sum=0

for key in dict:
    sum=sum+dict[key]

print("Dictionary=",dict)
print("sum of all items=",sum)