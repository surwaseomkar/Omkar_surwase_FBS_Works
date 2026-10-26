# Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage

# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
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


# Create Student Object
s1 = Student(101, "Omkar", 21, 82.5)

# Display Student Details
print("Student Details:")
s1.Display()

# Calculate Rank
print("Rank:", s1.CalculateRank())

# Display using __str__ method
print("\nUsing __str__ Method:")
print(s1)