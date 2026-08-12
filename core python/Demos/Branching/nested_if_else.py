gender = input('enter gender(M/F):')
age =int(input('Enter age:'))

if(gender =='F'):
    if(age >=18):
        print('Girl is eligible for marriafe.')
    else:
        print('pahele padhai kar le')
else:
    if(age >=21):
        print('Boy is eligible for marriage.')
    else:
        print('pahle kama lo.')


