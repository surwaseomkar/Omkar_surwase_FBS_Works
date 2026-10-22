# Python Program to Find the Union of two Lists

li1 = [1, 2, 3, 4]
li2 = [3, 4, 5, 6]

union =[]

for ind in range(0,len(li1)):
    if(li1[ind] not in union):
        union.append(li1[ind])

    for ind in range(0,len(li2)):
        if(li2[ind] not in union):
            union.append(li2[ind])

print("union=",union)
    