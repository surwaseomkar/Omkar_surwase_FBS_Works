# Write a program to create three lists of numbers, their squares
# and cubes

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square=[]
cube=[]

for ind in range(0,len(li)):
    square.append(li[ind]**2)
    cube.append(li[ind]**3)

print("numbers=",li)
print("squares=",square)
print("cubes=",cube)
