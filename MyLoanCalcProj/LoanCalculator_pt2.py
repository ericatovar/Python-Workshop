# Erica Tovar

# If you found the previous stage too easy, let's add something interesting. The best loans 
# are probably those with a 0% interest.

# Let's make some calculations for 0% loan repayments. The user might know the period of the 
# loan and want to calculate the monthly payment. Or the user might know the amount of the 
# monthly repayments and wonder how many months it will take to repay the loan in full.

# In this stage, we need to ask the user to input the loan principal amount. Then, the user 
# should indicate what needs to be calculated (the monthly payment amount or the number of months) 
# and enter the required parameter. After that, the loan calculator should output the value that 
# the user wants to know.

# Also, let’s assume we don't care about decimal places. If you get a floating-point expression as 
# a result of the calculation, you’ll have to do additional actions. Take a look at Example 4 where 
# you need to calculate the monthly payment. You know that the loan principal is 1000 and want to 
# pay it back in 9 months. The real value of payment can be calculated as:

# payment = principal/months = 1000/9 = 111.11...

# Of course, you can’t pay that amount of money. You have to round up this value and make it 112. 
# Remember that no payment can be more than the fixed monthly payment. If your monthly repayment 
# amount is 111, that would make the last payment 112, which is not acceptable. If you make a monthly 
# payment of 112, the last payment will be 104, which is fine. You can calculate the last payment as follows:

# lastpayment = principal - (periods - 1) * payment = 1000 - 8 * 112 = 114

# In this stage, you need to count the number of months or the monthly payment. If the last payment 
# differs from the rest, the program should display the monthly payment and the last payment.

### Objective ###
# The behavior of your program should look like this:

# 1) Prompt a user to enter their loan principal and choose which of the two parameters 
#    they want to calculate – the number of monthly payments or the monthly payment amount.
# 2) To perform further calculations, you'll also have to ask for the required missing value.
# 3) Finally, output the results for the user.

# NOTE: When you output how many months it will take to repay the loan, mind the grammar of 
# the sentence. For example, if it will take just one month to repay it, you should output: 
# "It will take 1 month to repay the loan" (using the singular form of "month"). In other cases, 
# use the plural form of "month": "It will take 7 months to repay the loan".

### Output ###
# NOTE: The greater-than symbol followed by a space (> ) represents the user input. Note that this is not part of the input.

# Example 1

# Enter the loan principal:
# > 1000
# What do you want to calculate?
# type "m" - for number of monthly payments,
# type "p" - for the monthly payment:
# > m
# Enter the monthly payment:
# > 150

# It will take 7 months to repay the loan

# Example 2

# Enter the loan principal:
# > 1000
# What do you want to calculate? 
# type "m" for number of monthly payments,
# type "p" for the monthly payment:
# > m
# Enter the monthly payment:
# > 1000

# It will take 1 month to repay the loan

# Example 3

# Enter the loan principal:
# > 1000
# What do you want to calculate?
# type "m" for number of monthly payments,
# type "p" for the monthly payment:
# > p
# Enter the number of months:
# > 10

# Your monthly payment = 100

# Example 4

# Enter the loan principal:
# > 1000
# What do you want to calculate?
# type "m" for number of monthly payments,
# type "p" for the monthly payment:
# > p
# Enter the number of months:
# > 9

# Your monthly payment = 112 and the last payment = 104.

### Write here ###
from math import ceil

principal = int(input("Enter your loan principal: ")) 
calculate = input("What would you like to calculate? Enter 'p' for monthly payment, or enter 'm' for number of monthly payments: ")

if calculate == "p":
    num = input("Enter the number of months: ")
    payment = ceil( principal / int(num))
    lastpayment = (principal - (int(num) - 1) * payment)
    print("Your monthly payment is {}, and your last payment is {}.".format(payment, lastpayment))
elif calculate == "m":
    months = input("Enter your monthly payment: ")
    permonth = principal / int(months)
    if (permonth == 1):
        mon = "month"
    else:
        mon = "months"
    print("It will take {} {} to repay the loan".format(permonth, mon))