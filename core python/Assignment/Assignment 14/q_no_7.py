# Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

set1={10,20,30,40,50}
set2={60,70,80,90}

print("First set=",set1)
print("Second set=",set2)

print("Numbers missing in second set=",set1-set2)
print("Numbers missing in first set=",set2-set1)