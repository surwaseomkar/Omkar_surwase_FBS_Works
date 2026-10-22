# Write a program print following patterns:
#A
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

for i in range(n - 1,0,-1):
    print(" " * (n - i)+ "* " * i)

#B
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*",end=" ")
    print()

#C
n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#D
n = 5

for i in range(1 ,n + 1):
    print(" " * (n - i), end=" ")

    for j in range(i, 2 * i):
        print(j, end=" ")

    for j in range(2 * i - 2, i - 1, - 1):
        print(j,end=" ")
    print()

#E

n = 5

for i in range(1, n + 1):
    print(" " * (n -i),end ="")

    if i ==1:
        print(1)
    elif i==n:
        for j in range(1, n + 1):
            print(j, end=" ")
        print()
    else:
         print(1,end=" ")
         print(" " * (2 * i -3),end="")
         print(i)

#F

n = 5

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1:
            print(j,end=" ")
        elif j == 1:
            print(i,end=" ")
        elif j == n - i + 1:
            print(n,end=" ")
        else:
            print(" ", end=" ")
    print()

# G
n = 5

for i in range(1, n +1):
    print(" " * (n -i), end="")

    for j in range(1, i + 1):
        print(j,end=" ")

    for j in range(i -1, 0, -1):
        print(j,end=" ")
    print()

#H

n = 7
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(1,n+1):
        print(" ",end=" ")
    n-=2
    for j in range(i,0,-1):
        if(i!=5 or j!=5):
         print(j,end=" ")
    print()