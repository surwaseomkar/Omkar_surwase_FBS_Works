#Accept age of five people and also per person ticket amount and then calculate total 
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

no=int(input("enter the no you want to tecket for:"))
totalamount=0
i=1
while i<no:
    age=int(input(f'enter the tkp of {i}st person:'))
    tkp=int(input(f'enter the tkp of {i}st person:'))
    if age<12:
        discount=tkp*(30/100)
        print('passanger get disscount of:',discount)
        totalamount=totalamount+(tkp-discount)
    elif age>59:
        discount=tkp*(50/100)
        print('passanger get discount:',discount)
    else:
        totalamount=totalamount+tkp
        print('you did not get any discount')
        i+=1
    print(totalamount)