# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class product:
    def __init__(self,pid=0,pname="",price=0,quantity=0):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity

    def __del__(self):
        print("Destructor called")

    def showbook(self):
        print("Product ID=",self.pid)
        print("product Name=",self.pname)
        print("price=",self.price)

        print("Quantity=",self .quantity)

p1=product()
p1.showbook()

p2=product(101,"Laptop",50000,2)
p2.showbook()