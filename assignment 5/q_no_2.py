# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n=int(input("enter number of student:"))
total_percentage=0

for i in range(n):
    m1=int(input("enter mark of 1 subject:"))
    m2=int(input("enter mark of 2 subject:"))
    m3=int(input("enter mark of 3 subject:"))
    m4=int(input("enter mark of 4 subject:"))
    m5=int(input("enter mark of 5 subject:"))

    total_mark=m1+m2+m3+m4+m5
    percentage=total_mark /5

    print("percentage=",percentage)
    total_percentage=total_percentage+percentage
    average=total_percentage/n

    print("average percentage is",average)
