
# Count the number of spaces in a string (take input from user)

text = input("Enter a string: ")
spaces = sum(1 for i in text if i ==' ')
print("Number of spaces:",spaces)