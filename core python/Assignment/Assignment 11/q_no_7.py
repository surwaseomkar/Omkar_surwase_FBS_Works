# Python Program to Find the Intersection of Two Lists

li1=[1, 2, 3, 4, 5]
li2=[3, 4, 5, 6, 7]

intersection=[]
for ind in range(0,len(li1)):
    if(li1[ind] in li2):
        intersection. append(li1[ind])

print("Intersection=",intersection)