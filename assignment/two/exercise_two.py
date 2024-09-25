import math


def CircleArea(radius):
    return math.pi * radius**2


radius = float(input("Enter the radius of the circle: "))
area = CircleArea(radius)

print("The area of the circle is:", area)
