# Write a program to find the second largest element in the list.

li = [ 30, 24, 90, 82,99, 55, 22, 33]
max = li[0]
for ind in range(1, len(li)):
    if li[ind] > max:
        max = li[ind]

second = li [0]

for ind in range (0,len(li)):
    if li [ind] != max and li [ind]  > second:
           second = li[ind]


print("second largest =",second)