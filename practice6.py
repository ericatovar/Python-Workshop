from matplotlib import pyplot as plt
import numpy as np

# Name: Erica Tovar

# Create a plot of the function y = 8 * sinc(x)
# Include a proper title, axis labels, legend, and a grid
# Customize the color and style for the line
# HINT: line styles include the following [ '-' | '--' | '-.' | ':' | 'steps' | ...] and are included in
#       the same string as the color change ex: 'b--'

### Write here ###
x = np.linspace(0, 50, 1000)
y = (8 * np.sinc(x))
plt.plot(x, y, "g-", label = "y = 8 * sinc(x)")
plt.title("Graph of Function")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.legend()

#--------------------------------------------------------------------------------------------------------

# Create a 3D plot of the same function as the previous problem
# Use the following to create the 3D plot:

# ax = plt.figure().add_subplot(projection='3d')
# ax.plot(x, y, zs=0, zdir='y')

# NOTE: x and y should be the x-axis and y-axis data from the previous problem

# For extra fun, make a for loop that will run in a range using linspace() and plot
# multiple sinc() functions in the xz plane at different values of y

### Write Here ###
x = np.linspace(0, 50, 1000)
ax = plt.figure().add_subplot(projection = "3d")
ax.plot(x, 8 * np.sinc(x), zs = 0, zdir = "y")

plt.title("3D Plot of Function")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

for i in range(5):
  ax.plot(x, 8 * np.sinc(x), zs=i, zdir="y")
plt.show()
np.linspace()