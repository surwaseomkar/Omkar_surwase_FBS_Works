# Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

list=[1,2,3,4,5,6]
value=7

for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]+list[j]==value:

         print("pair=",list[i],list[j])