# Calculate the cost of painting the following building’s walls (both interior and 
# exterior). You need to accept area (one wall) and cost of both interior and 
# exterior wall. 
# (Note: 1. Below diagram is of two joint rooms.
#  2. It is upper view of building.)

area =int(input("enter area of one wall:"))
interior_cost=int(input("enter interior wall cost:"))
exterior_cost=int(input("enter exterior wall cost:"))

interior_total = area*8*interior_cost
exterior_total = area*6*exterior_cost

total_cost = interior_total+exterior_total

print("Interior painting cost=",interior_total)
print("Exterior painting cost=",exterior_total)
print("Total painting cost=",total_cost)