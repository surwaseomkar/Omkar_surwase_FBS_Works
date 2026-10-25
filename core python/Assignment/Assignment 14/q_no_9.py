# Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

li=[1,2,3,4,5,6]
target=10

for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        for k in range(j+1,len(li)):
            if(li[i]+li[j]+li[k]==target):

             print(li[i],li[j],li[k])