# Create a class Book with members as bid,bname,price and author.Add following
# # methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.





class Book:
    count = 0

    def __init__(self, bid=None, bname=None, price=None, author=None):
        if bid is None:
            self.bid = 0
            self.bname = "Not Available"
            self.price = 0.0
            self.author = "Not Available"
        else:
            self.bid = bid
            self.bname = bname
            self.price = price
            self.author = author

        Book.count += 1

    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Book Price:", self.price)
        print("Book Author:", self.author)
        print("------------------------")

    def __del__(self):
        print("Book object destroyed:", self.bid)


# Parameterless Constructor
b1 = Book()

# Parameterized Constructor
b2 = Book(101, "Python Programming", 500, "Guido van Rossum")
b3 = Book(102, "Java Programming", 600, "James Gosling")

# Display Book Details
print("Book 1 Details:")
b1.ShowBook()

print("Book 2 Details:")
b2.ShowBook()

print("Book 3 Details:")
b3.ShowBook()

# Display Total Objects Created
print("Total Books Created:", Book.count)

# Delete Objects
del b1
del b2
del b3

















class Book:
    count = 0

    def __init__(self, bid=None, bname=None, price=None, author=None):
        if bid is None:
            self.bid = 0
            self.bname = "Not Available"
            self.price = 0.0
            self.author = "Not Available"
        else:
            self.bid = bid
            self.bname = bname
            self.price = price
            self.author = author

        Book.count += 1

    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Book Price:", self.price)
        print("Book Author:", self.author)
        print("------------------------")

    def __del__(self):
        print("Book object destroyed:", self.bid)


# Parameterless Constructor
b1 = Book()

# Parameterized Constructor
b2 = Book(101, "Python Programming", 500, "Guido van Rossum")
b3 = Book(102, "Java Programming", 600, "James Gosling")

# Display Book Details
print("Book 1 Details:")
b1.ShowBook()

print("Book 2 Details:")
b2.ShowBook()

print("Book 3 Details:")
b3.ShowBook()

# Display Total Objects Created
print("Total Books Created:", Book.count)

# Delete Objects
del b1
del b2
del b3







class Book:
    count = 0

    def __init__(self, bid=None, bname=None, price=None, author=None):
        if bid is None:
            self.bid = 0
            self.bname = "Not Available"
            self.price = 0.0
            self.author = "Not Available"
        else:
            self.bid = bid
            self.bname = bname
            self.price = price
            self.author = author

        Book.count += 1

    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Book Price:", self.price)
        print("Book Author:", self.author)
        print("------------------------")

    def __del__(self):
        print("Book object destroyed:", self.bid)


# Parameterless Constructor
b1 = Book()

# Parameterized Constructor
b2 = Book(101, "Python Programming", 500, "Guido van Rossum")
b3 = Book(102, "Java Programming", 600, "James Gosling")

# Display Book Details
print("Book 1 Details:")
b1.ShowBook()

print("Book 2 Details:")
b2.ShowBook()

print("Book 3 Details:")
b3.ShowBook()

# Display Total Objects Created
print("Total Books Created:", Book.count)

# Delete Objects
del b1
del b2
del b3