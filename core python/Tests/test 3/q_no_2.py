# Write a program to calculate the sum of following series
# where n is input by user.
# 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!

n = int(input("Enter the value of n: "))
sum = 0
fact = 1
for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (i / fact)

print("sum of series =",sum)