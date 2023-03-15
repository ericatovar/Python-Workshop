import random

# Name: Erica Tovar

# Convert and print the following variables as an int first and then a character

x = random.uniform(97,122)
y = random.uniform(97,122)
z = random.uniform(97,122)

### Write here ###
x = int(x)
y = int(y)
z = int(z)
print(x)
print(y)
print(z)
x = chr(x)
y = chr(y)
z = chr(z)

#--------------------------------------------------------------------------------------------------------

# Declare a valid variable with the value 'python', then fix the declared variable so it has a valid name

### Write here ###
MyPyth = 'python'
MyVar = '3.10'

#--------------------------------------------------------------------------------------------------------

# Change the data type of either variable above and print the following: 'python3.10'

### Write here ###
print(MyPyth + MyVar)

#--------------------------------------------------------------------------------------------------------

# Convert the following variables so the output of the function returns an integer
# (don't redeclare it as an int)
base = 2.000
exp = '6'

### Write here ###
base = int(base)
exp = int(exp)

result = int(pow(base,exp))

#print('2 raised to the 6 is:', result)
print('2 raised to the 6 is:', result)
#--------------------------------------------------------------------------------------------------------

# Use the result from above and divide it by 65, then print the character it represents on ASCII
result = int(result/65)
### Write here ###
print(chr(result))
