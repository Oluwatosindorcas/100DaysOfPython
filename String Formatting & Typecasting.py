# Calculate the volume of a Sphere.
# volume of a sphere = (4/3) * π * r3
import math
pi = math.pi
radius = float(input("Enter the radius of the sphere: "))
volumeOfASphere = (4 / 3) * pi * math.pow(radius, 3)
print(f"The volume of a sphere with {radius}cm is  {volumeOfASphere}cm")


# Calculate the length of a hypotenuse in a right triangle.
# length of a hypotenuse = square root(a2 + b2)

import math
adjacent = float(input("Enter the adjacent side of the right-angled triangle: "))
adjacentSquared = math.pow(adjacent, 2)
opposite = float(input("Enter the opposite side of the right-angled triangle: "))
oppositeSquared = math.pow(opposite, 2)
lengthOfAHypotenus = math.sqrt(adjacentSquared + oppositeSquared)
print(f"The length of the hypotenus in a right-angled triangle with an adjacent side of {adjacentSquared}cm and opposite side of {oppositeSquared}cm is {lengthOfAHypotenus}cm")


# Calculate the surface area of a cylinder
# 2 * π * r * (r + h)
import math

radOfTheCylinder = float(input("Enter the radius of the cylinder: "))
heightOfTheCylinder = float(input("Enter the height of the cylinder: "))
areaOfACylinder = 2 * math.pi * radOfTheCylinder * (radOfTheCylinder + heightOfTheCylinder)
print(f"The area of a cylinder with the radius {radOfTheCylinder}cm and height {heightOfTheCylinder}cm is {areaOfACylinder}cm")


# Calculate the Quadratic formulae for 3 given numbers.

# using the quadratic formula = x = (-b +- sqrt(b2 -4ac))2a
# solving quadratic equation means getting two answers in both positive and negative
a = float(input("Enter the value of the first coefficient a: "))
b = float(input("Enter the value of the second coefficient b: "))
c = float(input("Enter the value of the third coefficient c: "))
#x1 = (-b + sqrt(b2 -4ac))/2a
#x2 = (-b - sqrt(b2 -4ac))/2a

#d =sqrt(b2 -4ac)
import math
d = math.sqrt(b**2 - 4*a*c)
#x1 = (-b + d)/2a
#x1 = (-b - d)/2a
x1 = (-b + d)/(2 * a)
x2 = (-b - d)/(2 * a)
print(f"First Root  of the quadratic equation is {x1}")
print(f"Second Root  of the quadratic equation is {x2}")
print(f"The roots of a quadratic equation with coefficients {a}, {b}, {c} is {x1} and {x2}")



# Calculate the area of a Trapezoid.
#area of a trapezoid = 1/2 * (b1 + b2) * h
base1 = float(input("Enter the first base of the trapezoid: "))
base2 = float(input("Enter the second base of the trapezoid: "))
height0fTheTrapezoid = float(input("Enter the height of the trapezoid: "))
areaOfTheTrapezoid = 1 / 2 * (base1 + base2) * height0fTheTrapezoid
print(f"The area of a Trapezoid with first base as {base1}cm  and second base as {base2}cm is {height0fTheTrapezoid}cm")