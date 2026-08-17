# WAP to print Armstrong number within a given range

start=int(input("enter a number:"))
end=int(input("enter a number:"))

for i in range(start,end+1):
    temp=i
    digits=len(str(i))
    total=0

    while temp>0:
        digit=temp%10
        total=total+digit**digits
        temp=temp//10
    if total==i:
       print(i)