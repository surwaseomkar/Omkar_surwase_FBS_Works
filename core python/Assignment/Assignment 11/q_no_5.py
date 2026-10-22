# Python Program to Sort a List According to the Length of the Elements
# within the list.

li=["apple","cat","banana","dog","elephant"]
for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if(len(li[i])>len(li[j])):
            li[i],li[j]=li[j],li[i]

print("sorted list=",li)