# Remove all of the vowels in a string (take input from user)

text = input("Enter a string: ")

result = ''.join([i for i in text if i.lower() not in 'aeiou'])
print("String without vowels:",result)

