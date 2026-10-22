#Sum of all prime numbers between 1 to n

def prime_sum(n):
    sum = 0

    for num in range(2, n + 1):
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1

        if count ==2:
            sum = sum + num
    return sum 
n = int(input("enter n:"))
result = prime_sum(n) 
print("sum of prime numbers =", result)      


