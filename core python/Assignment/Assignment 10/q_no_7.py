#Write a program to create a new list from existing list which contains cube of
# each number of list.

li = [2, 3, 4, 5, 6]
cube = []
for ind in range(0, len(li)):
    n = li[ind]
    c = n * n * n
    cube = cube + [c]
print("original list =",li)
print("cube list =",cube)