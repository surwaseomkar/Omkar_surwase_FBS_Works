# Python Program to Remove the Given Key from a Dictionary

dict={"name":"rohit","age":"23","city":"pune"}

key=input("Enter the key to remove:")

if(key in dict):
    del dict[key]

    print("New dictionary=",dict)