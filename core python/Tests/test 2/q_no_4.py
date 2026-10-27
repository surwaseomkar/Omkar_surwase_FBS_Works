# Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.



length = float(input("Enter wall length: "))
height = float(input("Enter wall height: "))
rate = float(input("Enter painting rate per sq.m: "))

area = 4 * length * height
cost = area * rate

print("Total area of walls:", area, "sq.m")
print("Total cost of painting:", cost)