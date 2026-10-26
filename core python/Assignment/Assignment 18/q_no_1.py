# Create a class Complex Number with data members as real and imag and add
# following methods :

# a. Constructor
# b. Destructor
# c. Overload +,- operator

class ComplexNumber:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __add__(self,other):
        r = self.real + other.real
        i = self.imag + other.imag
        return ComplexNumber(r,i)

    def __sub__(self,other):
        r = self.real - other.real
        i = self.imag - other.imag
        return ComplexNumber(r,i)

    def __str__(self):
        return f"{self.real} +{self.imag} i"

    def __del__(self):
        print("ComplexNumber object destroyed")


#create objects
c1 = ComplexNumber(10,5)
c2 = ComplexNumber(4,2)


# Display objects
print("First Comolaex Number:",c1)
print("Second Complex Number:",c2)

#Addition 
c3 = c1 + c2
print("Addition:",c3)

# substraction
c4 = c1 - c2
print("Substraction:",c4)