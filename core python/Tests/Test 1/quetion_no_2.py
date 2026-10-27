# Write a program to calculate simple interest based on Principal, Rate and Time 
# (SI = P*R*T/100)

p = int(input("Enter principal:"))
r =int(input("Enter rate:"))
t =int(input("Enter time:"))

si = (p*r*t)/100
print("Simple Interest=",si)