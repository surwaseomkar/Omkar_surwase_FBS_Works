#Python Program to Find the Second Largest Number in a List Using Bubble Sort

li=[10, 5, 20, 8, 15]

for i in range(0,len(li)):
    for j in range(0,len(li)-i-1):
        if(li[j]>li[j+1]):
            li[j],li[j+1]=li[j+1],li[j]

print("sorted list=",li)
print("second largest number=",li[-2])