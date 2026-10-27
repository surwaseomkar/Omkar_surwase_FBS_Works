# write a function to which we pass a parametere and print the factors of a given number 

def factors(n):
    for i in range(1, n + 1):
        if n % i==0:
            print(i, end=" ")

n = int(input("Enter a number: "))
print("Factors of",n,":",end=" ")
factors(n)