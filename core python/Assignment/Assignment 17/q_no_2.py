# Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks


# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method



class Student:
    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Student Name: ")
        self.Age = int(input("Enter Student Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def Display(self):
        print("Student ID:", self.StudentId)
        print("Student Name:", self.Name)
        print("Student Age:", self.Age)
        print("Percentage:", self.Percentage)

    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 35:
            return "Pass Class"
        else:
            return "Fail"

    def __str__(self):
        return (
            f"Student ID: {self.StudentId}\n"
            f"Name: {self.Name}\n"
            f"Age: {self.Age}\n"
            f"Percentage: {self.Percentage}%"
        )


class EnggStudent(Student):

    def __init__(self, StudentId, Name, Age, Percentage,
                 Branch, InternalMarks):
        super().__init__(StudentId, Name, Age, Percentage)
        self.Branch = Branch
        self.InternalMarks = InternalMarks

    def Accept(self):
        super().Accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = float(input("Enter Internal Marks: "))

    def Display(self):
        super().Display()
        print("Branch:", self.Branch)
        print("Internal Marks:", self.InternalMarks)

    def CalculateRank(self):
        total = self.Percentage + self.InternalMarks

        if total >= 150:
            return "Distinction"
        elif total >= 120:
            return "First Class"
        elif total >= 100:
            return "Second Class"
        elif total >= 70:
            return "Pass Class"
        else:
            return "Fail"

    def __str__(self):
        return (
            super().__str__()
            + f"\nBranch: {self.Branch}"
            + f"\nInternal Marks: {self.InternalMarks}"
        )


# Create EnggStudent Object
e1 = EnggStudent(
    101,
    "Omkar",
    21,
    80,
    "Computer Science",
    18
)

# Display Student Details
print("Engineering Student Details:")
e1.Display()

# Calculate Rank
print("Rank:", e1.CalculateRank())

# Display using __str__
print("\nUsing __str__ Method:")
print(e1)