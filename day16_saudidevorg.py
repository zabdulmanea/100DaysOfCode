# Python Tuples - part 1
""" A tuple is a collection which is ordered and unchangeable
and it's written with round brackets ()
"""

# Create an empty tuple
thistuple = ()
print("Empty tuple:", thistuple)
print("---------------------------------------------")

# Create a tuple with one element
thistuple = ("Apple",)
print("Tuple with one element:", thistuple)
print("---------------------------------------------")

# Create a Tuple with numbers
thistuple = (1, 34.6, 23.09, 5, 6, 1, 34.67)
print("The tuple with inregers & decimal:", thistuple)
print("---------------------------------------------")

# Create a Tuple with different data types
thistuple = (1, 34.6, "Apple", 2, "Orange")
print("The tuple different data types:", thistuple)
print("---------------------------------------------")

# Create a Tuple with strings
thistuple = ("Apple", "Banana", "Cherry")
print("The tuple with strings:", thistuple)
print("---------------------------------------------")

# Access Tuple Items
# 1. Access one item
print("The second item is", thistuple[1])
print("---------------------------------------------")

# 2. Access Multiple items
print("The first and second are:", thistuple[0:2])
print("---------------------------------------------")

# Change Tuple Values
# thistuple[2] = "Orange"   # TypeError: 'tuple' object does not support item assignment
# cannot change items to because tuples are unchangeable

# Loop Through a Tuple
print("The tuple items are:")
for item in thistuple:
    print(item)
print("---------------------------------------------")

# Add Items
# thistuple[3] = "Orange"   # TypeError: 'tuple' object does not support item assignment
# cannot add items to it because tuples are unchangeable

# Remove Item
# del thistuple[0]  # TypeError: 'tuple' object doesn't support item deletion
# cannot remove items because tuples are unchangeable

# Delete the Tuple Completely
del thistuple
# print(thistuple) # NameError: name 'thistuple' is not defined
