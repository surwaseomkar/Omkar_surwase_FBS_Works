# Write a program to create a duplicate of an existing list. It should not point to
# same list.

li =[30, 24, 90, 82, 99]
new = []
for ind in range(0, len(li)):
    new = new +[li[ind]]
print("original list =",li)
print("duplicate list =",new)

new[0] = 100

print("after changing duplicates list")
print("original list =", li)
print("duplicates list =", new)