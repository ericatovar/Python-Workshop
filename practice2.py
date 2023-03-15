# Erica Tovar
from cmath import pi
import math
from tkinter import Variable

# Calculate the area of a cylinder given the following radius and height and store the result in a variable called result
# Format the result to print 'The area of a cylinder with a radius of {r} and a height of {h} is {answer}.'
# Round answer to three decimal points in print statement as well.

r = 3
h = 14

### Write here ###
result = (2 * math.pi * r * h) + (2 * math.pi * (r * r))
print('The area of a cylinder with a radius of {r} and a height of {h} is {result:.3f}'.format(r = r, h = h, result = result))

#--------------------------------------------------------------------------------------------------------

# Write a program that takes in a temperature in Celsius from the user and converts it to Farenheit.
# Print a statement that shows the conversion between the measurements.
# Use a math function to also round down the result in Farenheit.
# \N{DEGREE SIGN} optional to put a degree symbol

### Write here ###
Celcius = float(input("Enter temperature in Celsius here: "))
Farenheit = math.floor(Celcius * (9/5) + 32)
print('The temperature in farenheit is: {:.1f}\N{DEGREE SIGN}.'.format(Farenheit))

#--------------------------------------------------------------------------------------------------------

# Write a program that finds the roots of a quadratic function based on coefficients entered by the user.
# Quadratic equation: ax^2 + bx + c
# Print the quadratic equation that was created and the roots that were solved for.
# Round to two decimals for the roots

### Write here ###
a = float(input('Enter value for a here: '))
b = float(input('Enter value for b here: '))
c = float(input('Enter value for c here: '))

Discriminant = (b * b) - 4 * a * c
if Discriminant > 0:
    root_1 = (-b + math.sqrt((b * b) - 4 * a * c))/(2 * a)
    root_2 = (-b - math.sqrt((b * b) - 4 * a * c))/(2 * a)
    print('Root 1 is located at x = {root_1:.2f}.'.format(root_1 = root_1))
    print('Root 2 is located at x = {root_2:.2f}.'.format(root_2 = root_2))
elif Discriminant == 0:
    root_1 = (-b) / 2 * a
    print('The root is located at x = {root_1:.2f}.'.format(root_1 = root_1))
elif Discriminant < 0:
    print('No real roots exist.')