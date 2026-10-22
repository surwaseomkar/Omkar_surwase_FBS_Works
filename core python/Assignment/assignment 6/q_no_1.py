#Write a program print following patterns:
#a. 
for i in range(1,6):
    for j in range(1,6):
        if i ==1 or i == 5 or j == 1 or j ==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# # #b.
num = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(num,end=" ")
        num = num +1
    print()
# # #c.
for i in range(1,5):
    for j in range(1,i+1):
        if j == 1 or j == i:
            print(1, end=" ")
        elif i == 3:
            print(2, end=" ")
        else:
         print(3, end=" ")
    print()

# #d.
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j), end=" ")
    print()

#     #e.
for i in range(1,6):
    for j in range(1,i+1):
         print('*',end=' ')
    for j in range(1,i):
        print('*',end=' ')
    print()

# #f
for i in range(1,6):
    for j in range(1,2*i):
        print(j, end=" ")
    print()

# #g
for i in range(1,6):
    for j in range(1,i):
        print(chr(64+j), end=" ")
    for j in range(i,2*i):
        print(chr(64+j), end=" ")
    print()