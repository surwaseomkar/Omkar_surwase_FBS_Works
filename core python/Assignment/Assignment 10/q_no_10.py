# Write a program to remove all occurrences of a given element in the list.

li =[1,2,3,4,2,5,6,2]

element = 2
new =[]
for ind in range(0,len(li)):
    if(li[ind]!=element):
        new.append(li[ind])

for ind in range(0,len(li)):
    if(li[ind]!=element):
        new.append(li[ind])

print("original list=",li)
print("list after removing occurrences==",new)
