# Create another package “TY” which has a class TYMarks (Theory,
# Practical).

class TYMark:
    def __init__(self,theory,practical):
        self.theory=theory
        self.practical=practical
    def display(self):
        print(f"theory={self.theory}\tpractical={self.practical}")

    