#Convert the time entered in hh,min and sec into seconds

hour=int(input('enter a hour:'))
minite=int(input('enter a minite:'))
second=int(input('enter a second:'))
second=(hour*3600+minite*60)+second
print('total second',second)