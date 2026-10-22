# Write a program to find maximum and minimum element in a list.

li = [10, 24, 90, 82, 99, 55, 22, 33]

max = li[0]
min = li[0]

for ind in range(1, len(li)):
    if li[ind] >max:
        max = li[ind]

    if li[ind] < min:
        min = li[ind]

print("maximum =",max)
print("minimum =",min)