#Write a program to reverse the list.

li = [30, 24, 90, 82, 99, 55, 22, 33]

rev = []

for ind in range(len(li)-1, -1, -1):
    rev = rev + [li[ind]]

print("original list =",li)
print("reverse list =", rev)