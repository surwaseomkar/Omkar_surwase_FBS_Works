#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1=int(input('enter a mark sub1:'))
sub2=int(input('enter a mark sub2:'))
sub3=int(input('enter a mark sub3:'))
sub4=int(input('enter a mark sub4:'))
sub5=int(input('enter a mark sub5:'))


total=sub1+sub2+sub3+sub4+sub5
percantage=(total/500)*100
print('percntage',percantage)

if percantage>85:
    print("first class")
elif percantage>70:
    print("second class")
elif percantage>65:
    print("third class")
elif percantage>50:
    print("fourth class")
else:
    print("fail")







