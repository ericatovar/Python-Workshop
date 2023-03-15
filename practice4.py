from random import randint

# Name: Erica Tovar

# Create and print out a new list that only contains the integers from the given list below.

randList = [45, 2, 'true', True, 0, '100', 4, 2.01, 3.33, 86, False]

### Write here ##
intlist = []
for i in randList:
    if type(i) == int:
        intlist.append(i)
print("Integers: {}".format(intlist))
print()

#--------------------------------------------------------------------------------------------------------

# Given a list of random integers below, go through the list and place all even integers in one list
# and all odd integers in another. Print both lists once done.

randInts = []
for i in range(100):
    randInts.append(randint(0,999))

### Write here ###
evenint = []
oddint = []
for i in randInts:
    if i % 2 == 0:
        evenint.append(i)
    else:
        oddint.append(i)
print("Even numbers list: {}".format(evenint))
print()
print("Odd numbers list: {}".format(oddint))
print()

#--------------------------------------------------------------------------------------------------------

# Find the largest and smallest number from the following three lists. 
# Optional: print which list they came from as well as its index location.

nums1 = [-29, -81, 86, 45, 58, 187, 659, -11, 114, 3]
nums2 = [128, -100, 409, -110, 179, -102, 671, 95, 3, 86]
nums3 = [-118, 104, -13, 11, 320, 202, -32, 608, 372, -750]

### Write here ###
nums1.sort()
print ("The smallest number in nums1 is {}.".format(nums1[0]))
print ("The largest number in nums1 is {}.".format(nums1[-1]))
print()

nums2.sort()
print ("The smallest number in nums2 is {}.".format(nums2[0]))
print ("The largest number in nums2 is {}.".format(nums2[-1]))
print()

nums3.sort()
print ("The smallest number in nums3 is {}.".format(nums3[0]))
print ("The largest number in nums3 is {}.".format(nums3[-1]))
