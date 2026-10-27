# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

radius = 20
length = 50
width = 40
rate = 35

circle = 3.14 * radius
rectangle = length + 2 * width

perimeter = circle + rectangle
total_wire = perimeter * 5
cost = total_wire * rate

print("Total wire required:",total_wire,"m")
print("Total fencing cost: Rs,",cost)