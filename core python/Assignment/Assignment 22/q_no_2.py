# WAP a menu driven program to perform following operations using
# files :

# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.

import pickle
import os

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic


def add_record():
    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    emp = Emp(eid, ename, basic)

    with open("emp.dat", "ab") as f:
        pickle.dump(emp, f)

    print("Record added successfully!")


def search_record():
    eid = int(input("Enter Employee ID to search: "))

    if not os.path.exists("emp.dat"):
        print("Record not found!")
        return

    with open("emp.dat", "rb") as f:
        try:
            while True:
                emp = pickle.load(f)

                if emp.eid == eid:
                    print("Employee ID:", emp.eid)
                    print("Employee Name:", emp.ename)
                    print("Basic Salary:", emp.basic)
                    return

        except EOFError:
            print("Record not found!")


def delete_record():
    eid = int(input("Enter Employee ID to delete: "))
    records = []

    if os.path.exists("emp.dat"):
        with open("emp.dat", "rb") as f:
            try:
                while True:
                    emp = pickle.load(f)
                    if emp.eid != eid:
                        records.append(emp)
            except EOFError:
                pass

    with open("emp.dat", "wb") as f:
        for emp in records:
            pickle.dump(emp, f)

    print("Record deleted successfully!")


def edit_record():
    eid = int(input("Enter Employee ID to edit: "))
    records = []
    found = False

    if os.path.exists("emp.dat"):
        with open("emp.dat", "rb") as f:
            try:
                while True:
                    emp = pickle.load(f)

                    if emp.eid == eid:
                        emp.ename = input("Enter New Name: ")
                        emp.basic = float(input("Enter New Salary: "))
                        found = True

                    records.append(emp)
            except EOFError:
                pass

    with open("emp.dat", "wb") as f:
        for emp in records:
            pickle.dump(emp, f)

    if found:
        print("Record updated successfully!")
    else:
        print("Record not found!")


def display_all():
    if not os.path.exists("emp.dat"):
        print("No records found!")
        return

    with open("emp.dat", "rb") as f:
        try:
            while True:
                emp = pickle.load(f)
                print("Employee ID:", emp.eid)
                print("Employee Name:", emp.ename)
                print("Basic Salary:", emp.basic)
                print("--------------------")
        except EOFError:
            pass


while True:
    print("\n1. Add a Record")
    print("2. Search a Record")
    print("3. Delete a Record")
    print("4. Edit a Record")
    print("5. Display All Records")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        search_record()
    elif choice == "3":
        delete_record()
    elif choice == "4":
        edit_record()
    elif choice == "5":
        display_all()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")