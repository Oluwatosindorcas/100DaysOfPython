

# Calculate the volume of a Sphere where radius is 7cm.

# volume of a sphere = (4/3) * π * r3
import math
pi = math.pi
radius = 7
volumeOfASphere = (4 / 3) * pi * math.pow(7, 3)
print("The volume of a sphere: ", volumeOfASphere)

# Calculate the length of a hypotenuse in a right triangle where opposite is 5cm and adjacent is 3cm.
# length of a hypotenuse = square root(a2 + b2)


adjacent = 3
adjacentSquared = math.pow(adjacent, 2)
opposite = 5
oppositeSquared = math.pow(opposite, 2)
lengthOfAHypotenus = math.sqrt(adjacentSquared + oppositeSquared)
print("The length of a hypotenus: ", lengthOfAHypotenus)

# Calculate the surface area of a cylinder where radius is 5cm and height is 7cm
# 2 * π * r * (r + h)

radOfTheCylinder = 5
heightOfTheCylinder = 7
areaOfACylinder = 2 * math.pi * radOfTheCylinder * (radOfTheCylinder + heightOfTheCylinder)
print("The area of a cylinder: ", areaOfACylinder)

# Calculate the Quadratic formulae for 3 given numbers where a = 10, b = -9 and c = 6.
# using the quadratic formula = x = (-b +- sqrt(b2 -4ac))2a
# solving quadratic equation means getting two answers in both positive and negative
a = 10
b = -9
c = 6
#x1 = (-b + sqrt(b2 -4ac))/2a
#x2 = (-b - sqrt(b2 -4ac))/2a

#d =sqrt(b2 -4ac)
import cmath

d = cmath.sqrt(b**2 - 4*a*c)


#x1 = (-b + d)/2a
#x1 = (-b - d)/2a

x1 = (-b + d)/(2 * a)
x2 = (-b - d)/(2 * a)

print("Positive Root 1 of the quadratic equation: ", x1)
print("Negative Root 2 of the quadratic equation: ", x2)


# Calculate the area of a Trapezoid, where base1 = 2, base2 = 5 and height is 7cm
# area of a trapezoid = 1/2 * (b1 + b2) * h
base1 = 2
base2 = 5
height0fTheTrapezoid = 7
areaOfTheTrapezoid = 1 / 2 * (base1 + base2) * height0fTheTrapezoid
print("The area of a Trapezoid: ",  areaOfTheTrapezoid)


