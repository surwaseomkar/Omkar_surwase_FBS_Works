# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:
    discount = 10

    def __init__(self, pid=None, pname=None, price=None, quantity=None):
        if pid is None:
            self.pid = 0
            self.pname = "Not Available"
            self.price = 0.0
            self.quantity = 0
        else:
            self.pid = pid
            self.pname = pname
            self.price = price
            self.quantity = quantity

    def ShowBook(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Product Price:", self.price)
        print("Product Quantity:", self.quantity)
        print("Discount:", Product.discount, "%")
        print("Final Price:", self.apply_discount())
        print("---------------------------")

    def apply_discount(self):
        discount_amount = self.price * Product.discount / 100
        final_price = self.price - discount_amount
        return final_price

    def __del__(self):
        print("Product object destroyed:", self.pid)


# Parameterless Constructor
p1 = Product()

# Parameterized Constructor
p2 = Product(101, "Laptop", 50000, 2)
p3 = Product(102, "Mobile", 20000, 3)

# Display Product Details
print("Product 1 Details:")
p1.ShowBook()

print("Product 2 Details:")
p2.ShowBook()

print("Product 3 Details:")
p3.ShowBook()

# Delete Objects
del p1
del p2
del p3