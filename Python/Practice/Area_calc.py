import math

radius = input("Please enter a radius of a circle: ")
radius = float(radius)

Circle_Area = (22/7)*(pow(radius,2))
Circle_Area = round(Circle_Area,2)
print(f"Area of the circle is: {Circle_Area}")