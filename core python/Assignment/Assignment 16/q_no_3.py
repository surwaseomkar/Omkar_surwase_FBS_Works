# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.


class Shirt:
    rate = 10

    def __init__(self, sid=None, sname=None, stype=None, price=0, size="small"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.size = size

        if sid is None:
            self.price = 0
        else:
            self.price = price

        if sid is not None:
            if size.lower() == "small":
                self.price = price
            elif size.lower() == "medium":
                self.price = price + (price * Shirt.rate / 100)
            elif size.lower() == "large":
                self.price = price + (price * Shirt.rate * 2 / 100)
            elif size.lower() == "xlarge":
                self.price = price + (price * Shirt.rate * 3 / 100)

    def ShowBook(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Shirt Type:", self.stype)
        print("Shirt Size:", self.size)
        print("Shirt Price:", self.price)
        print("-------------------------")

    def __del__(self):
        print("Shirt object destroyed:", self.sid)


# Parameterless Constructor
s1 = Shirt()

# Parameterized Constructor
s2 = Shirt(101, "Cotton Shirt", "Formal", 1000, "small")
s3 = Shirt(102, "Cotton Shirt", "Formal", 1000, "medium")
s4 = Shirt(103, "Cotton Shirt", "Formal", 1000, "large")
s5 = Shirt(104, "Cotton Shirt", "Formal", 1000, "xlarge")

# Display Shirt Details
print("Shirt 1 Details:")
s1.ShowBook()

print("Shirt 2 Details:")
s2.ShowBook()

print("Shirt 3 Details:")
s3.ShowBook()

print("Shirt 4 Details:")
s4.ShowBook()

print("Shirt 5 Details:")
s5.ShowBook()

# Delete Objects
del s1
del s2
del s3
del s4
del s5