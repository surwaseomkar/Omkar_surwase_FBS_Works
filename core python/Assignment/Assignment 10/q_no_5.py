#Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

li = [30, 24, 90, 24, 99, 24, 22, 33]

num = int(input("Enter number = "))
count = 0
for ind in range(0, len(li)):
    if li [ind] == num:
        count = count + 1
if count > 0:
    print("element is present")
    print("count =", count)
else:
    print("element is not present")