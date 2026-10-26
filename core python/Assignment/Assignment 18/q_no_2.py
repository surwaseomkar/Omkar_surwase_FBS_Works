# Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator


class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self, other):
        total_cm = self.cm + other.cm
        total_m = self.m + other.m
        total_km = self.km + other.km

        total_m = total_m + (total_cm // 100)
        total_cm = total_cm % 100

        total_km = total_km + (total_m // 1000)
        total_m = total_m % 1000

        return Distance(total_km, total_m, total_cm)

    def __sub__(self, other):
        total1 = self.km * 100000 + self.m * 100 + self.cm
        total2 = other.km * 100000 + other.m * 100 + other.cm

        if total1 < total2:
            raise ValueError("First distance must be greater than or equal to second distance")

        difference = total1 - total2

        km = difference // 100000
        difference = difference % 100000

        m = difference // 100
        cm = difference % 100

        return Distance(km, m, cm)

    def __str__(self):
        return f"{self.km} km, {self.m} m, {self.cm} cm"

    def __del__(self):
        print("Distance object destroyed")


# Create objects
d1 = Distance(5, 600, 80)
d2 = Distance(2, 500, 50)

# Display distances
print("First Distance:", d1)
print("Second Distance:", d2)

# Addition
d3 = d1 + d2
print("Addition:", d3)

# Subtraction
d4 = d1 - d2
print("Subtraction:", d4)