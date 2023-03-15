#Erica Tovar
import math

# Write a program that takes in 4 numbers (each is > 0) from the user and print the largest number

### Write here ###
num_1 = float(input("Enter your first number here: "))
num_2 = float(input("Enter your second number here: "))
num_3 = float(input("Enter your third number here: "))
num_4 = float(input("Enter your fourth number here: "))

if (num_1 and num_2 and num_3 and num_4) <= 0:
    print("Please only enter numbers greater than 0")
elif (num_1 > num_2) and (num_1 > num_3) and (num_1 > num_4):
    print("{num_1} is the greatest number.".format(num_1 = num_1))
elif (num_2 > num_1) and (num_2 > num_3) and (num_2 > num_4):
    print("{num_2} is the greatest number.".format(num_2 = num_2))
elif (num_3 > num_1) and (num_3 > num_2) and (num_3 > num_4):
    print("{num_3} is the greatest number.".format(num_3 = num_3))
elif (num_4 > num_1) and (num_4 > num_2) and (num_4 > num_3):
    print("{num_4} is the greatest number.".format(num_4 = num_4))

#--------------------------------------------------------------------------------------------------------

# Write a program that takes a number grade from the user and print the corresponding letter grade
# Include whether the letter is grade is plus or minus
# Ex: 100-95 -> A+, 84-80 -> B-, etc. , F can be excluded from plus or minus

### Write here ###
num_grade = float(input("Enter your number grade here: "))

if (num_grade >= 95):
    print("Your letter grade is A+.")
elif (num_grade <= 94) and (num_grade >= 90):
    print("Your letter grade is A-.")
elif (num_grade <= 89) and (num_grade >= 85):
    print("Your letter grade is B+.")
elif (num_grade <= 84) and (num_grade >= 80):
    print("Your letter grade is B-.")
elif (num_grade <= 79) and (num_grade >= 75):
    print("Your letter grade is C+.")
elif (num_grade <= 74) and (num_grade >= 70):
    print("Your letter grade is C-.")
elif (num_grade <= 69) and (num_grade >= 65):
    print("Your letter grade is D+.")
elif (num_grade <= 64) and (num_grade >= 60):
    print("Your letter grade is D-.")
else:
    print("Your letter grade is an F.")

#--------------------------------------------------------------------------------------------------------

# Create a basic calculator (+,-,*,/) that accepts two numbers and a mathematical operator from the user and 
# performs the calculation IF the numbers are even
# Make sure to print whether the program failed if either number is not even

### Write here ###
num_1 = float(input("Enter your first even number here: "))
num_2 = float(input("Enter your second even number here: "))
if num_1 % 2 == 1 or num_2 % 2 == 1:
    print("Please input only even numbers.")

if num_1 % 2 == 0 and num_2 % 2 == 0:
    operation = input("Use + - * / and enter what operation you would like to perform here: ")
    if operation == "+":
        sum = num_1 + num_2
        print("{num_1} + {num_2} is equal to {sum}.".format(num_1 = num_1, num_2 = num_2, sum = sum))
    elif operation == "-":
        difference = num_1 - num_2
        print("{num_1} - {num_2} is equal to {difference}.".format(num_1 = num_1, num_2 = num_2, difference = difference))
    elif operation == "*":
        product = num_1 * num_2
        print("{num_1} * {num_2} is equal to {product}.".format(num_1 = num_1, num_2 = num_2, product = product))
    elif operation == "/":
        quotient = num_1 / num_2
        print("{num_1} / {num_2} is equal to {quotient}.".format(num_1 = num_1, num_2 = num_2, quotient = quotient))