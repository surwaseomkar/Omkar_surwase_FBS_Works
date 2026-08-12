#Write a program to calculate profit or loss.

cp=int(input("enter cost price:"))
sp=int(input("enter selling price:"))
if sp>cp:
    profit=sp-cp
    print("profit=",profit)
elif sp<cp:
    loss=sp-cp
    print("loss=",loss)
else:
    print("no loss no profit:")