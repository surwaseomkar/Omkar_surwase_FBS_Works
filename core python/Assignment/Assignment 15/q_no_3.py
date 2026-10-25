# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class shirt:
    def __init__(self,sid=0,sname="",type="",price=0,size=""):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size

    def showbook(self):
        print("Shirt ID=",self.sid)
        print("Shirt Name=",self.sname)
        print("Type=",self.type)
        print("Price=",self.price)
        print("Size=",self.size)

s1=shirt()
s1.showbook()

print("------------------------------------------------")

s2=shirt(101,"Formal shirt","Formal",1200,"Large")
s2.showbook()