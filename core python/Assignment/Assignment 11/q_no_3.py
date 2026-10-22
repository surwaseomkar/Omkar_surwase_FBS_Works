#Python Program to Sort the List According to the Second Element in Sublist

li =[[1, 5], [2, 2], [3, 8], [4, 1]]

for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if(li[i][1]>li[j][1]):
            li[i],li[j]=li[j],li[i]


print("sorted list=",li)
