#Write a program to remove duplicates from the list.

li =  [90, 45, 21, 90, 21, 79, 43, 88]
new =[]
for ind in range(0, len(li)):
    found = 0
    for j in range(0, len(new)):
        if li[ind]== new[j]:
            found = 1
            break
    if found == 0:
        new = new +[li[ind]]
print("original list =",li)
print("list after removing duplicates =",new)