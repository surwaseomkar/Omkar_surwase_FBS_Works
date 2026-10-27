# Create object of student class (Outside SY & TY package) having roll
# number, name, SYMakrs and TYMarks. Add the marksof SY and TY
# Computer subjects and calculate grade ("A" for >=70, "B" for >=60,
# "C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result
# of the student in proper format.

from symark import SYMark
from tymark import TYMark


class Student:
    def __init__(self, rollno, name, sy, ty):
        self.rollno = rollno
        self.name = name
        self.sy = sy
        self.ty = ty

    def display(self):
        total = (self.sy.computer + self.sy.maths +
                 self.sy.electronics + self.ty.theory +
                 self.ty.practical)

        percentage = total / 5

        if percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        print("\n----- Student Result -----")
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("Computer:", self.sy.computer)
        print("Maths:", self.sy.maths)
        print("Electronics:", self.sy.electronics)
        print("Theory:", self.ty.theory)
        print("Practical:", self.ty.practical)
        print("Total Marks:", total, "/ 500")
        print("Percentage:", percentage, "%")
        print("Grade:", grade)

rollno=int(input("Enter the rollno:"))
name=input("Enter the name:")
computer=int(input("Enter the computer model:"))
math=int(input("Enter the math mark:"))
electronic=int(input("Enter the electronic mark:"))
theory=int(input("Enter the theory mark:"))
practical=int(input("Enter the practical mark:"))

sy = SYMark(computer, math, electronic)
ty = TYMark(theory, practical)

s1 = Student(rollno, name, sy, ty)
s1.display()