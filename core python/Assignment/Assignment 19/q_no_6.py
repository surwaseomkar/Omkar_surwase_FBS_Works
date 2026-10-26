# Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)

text = input("Enter a sentence: ")

result = {word: len(word) for word in text.split()}
print(result)