# Python Tuples - part 2
""" A tuple is a collection which is ordered and unchangeable
and it's written with round brackets ()
"""
# Create a fruits tuple
thistuple = ("Apple", "Banana", "Cherry")
print("The tuple is", thistuple)

# Check the Existence of an Item
print("Is Apple in the fruits tuple?", "Apple" in thistuple)

# Tuple Length
print("The fruits tuple length =", str(len(thistuple)))
print("---------------------------------------------")

# Repeat Item
applestuple = ("Apple",)*5
print("Apples tuple:", applestuple)  # tuple
print(type(applestuple))
print("---------------------------------------------")

# Repeat Item without using comma
orangestuple = ("Oranges")*5
print(orangestuple)  # string
print(type(orangestuple))
print("---------------------------------------------")

# + Operator in Tuple
x = (3, 4, 5, 6)
x = x + (1, 2, 3)
print(x)
print("---------------------------------------------")

# The tuple() Constructor
thistuple = tuple(("Apple", "Banana", "Cherry"))
print("Create a tuple using tuple():", thistuple)
print("---------------------------------------------")

# Convert the list items into tuple using tuple()
thislist = [1, 2, 3, "Lemon", "Orange"]
thistuple = tuple(thislist)
print("The list:", thislist)
print("Create a tuple from the list:", thistuple)
print("---------------------------------------------")

# Count the Number of Specific Item
thistuple = ("Apple", "Banana", "Apple", "Cherry", "Apple", "Orange")
print(thistuple)
print("Number of Apples =", thistuple.count("Apple"))

# The Index of an Item
print("The index of Cherry =", thistuple.index("Cherry"))
print("---------------------------------------------")
