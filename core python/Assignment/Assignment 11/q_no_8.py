# Print 1 to 100 in snakes and ladder pattern.

li=[]
for i in range(1, 101):
    li.append(i)

    for i in range(0,100,10):
        if(i//10%2==0):
            print(li[i:i+10])
        else:
            print(li[i:i+10][::-1])