from math import cos
from math import sqrt
from math import radians
from math import pi

# Name: Erica Tovar


# Write a function that takes in some integer greater than 0 as a parameter and checks
# whether the integer is prime. Print a statement, does not return anything.
# Hint: Loop through the integers previous
# Hint: 1 is not prime

### Write here ###
def isPrime (num):
  for x in range(2, num):
    if (num%x) == 0:
      print(num, "Your number is not Prime")
      break
  else:
      print(num, "Your number is Prime")

num = int(input("Input a positive number here to check if it's prime: "))
if num > 1:
  isPrime(num)
else:
  print("Please enter a positive number.")

print()

#--------------------------------------------------------------------------------------------------------

# Write a function that calculates the volume of a sphere. Then let the user input enter the radius for
# two spheres. Use the function to find and print which sphere is bigger, along with its volume up to two decimals.

### Write here ###
def sphereVol(r):
    return ((4/3.0) * pi * pow(r, 3))

r1 = float(input("Enter the radius of the first sphere here: "))
r2 = float(input("Enter the radius of the second sphere here: "))
v1 = sphereVol(r1)
v2 = sphereVol(r2)

if (v2 > v1):
    print(f"The volume of the second sphere is{v2: .2f}. It is greater than sphere 1.")
elif (v1 > v2):
    print(f"The volume of the first sphere is{v1: .2f}. It is greater than sphere 2.")

else:
    print(f"The volumes of both spheres is{v1: .2f}. They are equal to each other.")

#--------------------------------------------------------------------------------------------------------

# Write a function that finds the length of the third side of a triangle. Function should have three
# arguments: one side of triangle, another side, angle between the sides. Ask the user to input the 
# two sides and the angle between them in degrees. Return the answer as a float and print it outside of 
# the function, format to two decimal points.
# Hint: Use the law of cosines formula
# Hint: The cos() function only takes radians, so use radians() function for conversion

### Write here ###
def sideC():
    A = float(input("Enter the length of side A from a triangle here: "))
    B = float(input("Enter the length of side B from a the triangle here: "))
    angle = float(input("Enter a number for the angle between sides A and B here: "))
    angle = cos(radians(angle))
    C = sqrt((A * A)+(B*B) - 2*(A*B)*angle)
    return C
C = sideC()
print("The length of the third side of triangle is {:.2f}.".format(C))