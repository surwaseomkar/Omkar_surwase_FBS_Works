# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

total_amount=0
n=int(input("enter number of passenger:"))
ticket=int(input("enter price of ticket:"))

for i in range(n):
    age=int(input("enter age of passenger:"))
    if age<12:
        amount=ticket-ticket*30/100
    elif age<59:
        amount= ticket*50/100
    else:
        amount=ticket

        total_amount=total_amount+amount
    print("total ticket amount=",total_amount)