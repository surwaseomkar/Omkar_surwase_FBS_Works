# Write a program to print list after removing even numbers.

li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd=[]
for ind in range(0,len(li)):
    if(li[ind]%2!=0):
        odd.append(li[ind])

print("original list=",li)
print("list after removing even numbers=",odd)

