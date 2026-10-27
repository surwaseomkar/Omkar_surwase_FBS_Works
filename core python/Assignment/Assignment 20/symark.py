# create a package “SY” which has class SYMARKS (Computer Total,
# MathsTotal, ElectronicsTotal).

class SYMark:
    def __init__(self,computer, maths,electronics):
        self.computer=computer
        self.maths=maths
        self.electronics=electronics
    def display(self):
        print(f"computer={self.computer}\t maths={self.maths}\telectronics={self.electronics}")

    