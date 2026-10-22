#Sum of all odd numbers between 1 to n

def odd_sum(n):
    sum = 0

    for i in range(1, n + 1):
        if i % 2 !=0:
            sum = sum +i

    return sum

n = int(input("enter n:"))
result = odd_sum(n)
print("sum of odd numbers =",result)
