#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount

amount=int(input('enter a amount:'))
n2000=amount//2000
amount=amount%2000

n500=amount//500
amount=amount%500

n200=amount//200
amount=amount%200

n100=amount//100
amount=amount%100

n50=amount//50
amount=amount%50

print(f'2000 notes {n2000}, 500 notes {n500}, 200 notes {n200},100 notes {n100} ,50 notes {n50}')



