# Create a class College which has collection of students. Add the
# following methods :

# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method



class Student:
    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def __str__(self):
        return (
            f"Student ID: {self.StudentId}, "
            f"Name: {self.Name}, "
            f"Age: {self.Age}, "
            f"Percentage: {self.Percentage}%"
        )


class College:
    def __init__(self, number):
        self.students = []
        self.number = number

    def AddStudent(self, student):
        if len(self.students) < self.number:
            self.students.append(student)
            print("Student added successfully.")
        else:
            print("College is full.")

    def GetStudent(self, sid):
        for student in self.students:
            if student.StudentId == sid:
                return student
        return None

    def RemoveStudent(self, sid):
        student = self.GetStudent(sid)

        if student is not None:
            self.students.remove(student)
            print("Student removed successfully.")
        else:
            print("Student not found.")

    def __str__(self):
        if not self.students:
            return "No students in college."

        result = "College Student Details:\n"

        for student in self.students:
            result += str(student) + "\n"

        return result


# Create College Object
c1 = College(3)

# Create Student Objects
s1 = Student(101, "Omkar", 21, 80.5)
s2 = Student(102, "Rahul", 22, 75.5)
s3 = Student(103, "Amit", 21, 65.0)

# Add Students
c1.AddStudent(s1)
c1.AddStudent(s2)
c1.AddStudent(s3)

# Display All Students
print("\n", c1)

# Get Student
print("Search Student:")
student = c1.GetStudent(102)

if student is not None:
    print(student)
else:
    print("Student not found.")

# Remove Student
print("\nRemove Student:")
c1.RemoveStudent(101)

# Display Updated Collection
print("\nUpdated College Details:")
print(c1)