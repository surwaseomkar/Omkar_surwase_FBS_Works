#Python Program to Put Even and Odd elements of a List into two Different Lists

li =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=[]
odd=[]

for ind in range(0,len(li)):
    if(li[ind]%2==0):
        even.append(li[ind])
    else:
        odd.append(li[ind])

print("even element=",even)
print("odd element=",odd)
