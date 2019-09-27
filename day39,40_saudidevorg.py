# Exercises

""" Q1: Use recursion to calculate 5*5*5 """
def power_function(num, power):
    if power > 0:
        result = num * power_function(num, power-1)
    else:
        result = 1
    return result


print(power_function(5, 3))
print("------------------------------------")

""" # Q2: Create a list contains -4, -6, -5, -1, 2, 3, 7, 9, 88 
then use Lambda to print the positive numbers fom the list
"""
# the list
numlist = [-4, -6, -5, -1, 2, 3, 7, 9, 88]
print(numlist)
positive_numbers = []

# Lambda
isPositive = lambda num : num > 0

for num in numlist:
    if (isPositive(num)):
        positive_numbers.append(num)
print(positive_numbers)
print("------------------------------------")
