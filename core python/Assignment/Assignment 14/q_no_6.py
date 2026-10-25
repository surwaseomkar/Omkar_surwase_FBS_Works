# Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

numbers={1,2,3,4,5}

max_product=0

for num1 in numbers:
    for num2 in numbers:
        if num1 !=num2:
            product=num1*num2

            if product > max_product:
                max_product=product
                a=num1
                b=num2

print("set=",numbers)
print("Two numbers=",a+b)
print("Maximum product=",max_product)