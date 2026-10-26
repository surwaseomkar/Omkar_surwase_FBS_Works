# Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.



def palindrome():
    num=121
    if str(num)==str(num)[::-1]:
        yield num

gen=palindrome()
print(next(gen))