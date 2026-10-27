# Write a program to print first n prime numbers

n = int(input("Enter how many prime numbers: "))
for i in range(2, 1000):
    count = 0

    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    if count ==2:
        print(i,end=" ")
        n -=1

    if n ==0:
        break
