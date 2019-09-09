# Python Sets - Part 2

# create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Get the Length of a Set
print(len(thisset))

# Remove Item
# 1. remove an item from the set, using remove()
thisset.remove("banana")
print(thisset)

# remove an item doesn't exist in the set
# thisset.remove("orange") # KeyError: 'orange'

# 2. remove an item from the set, using discard()
thisset.discard("cherry")
print(thisset)

# remove an item doesn't exist in the set
thisset.discard("orange")  # discard() will NOT raise an error

# 3. remove random item using pop()
thisset = {"apple", "banana", "cherry"}
print("The removed item is ", thisset.pop())
print(thisset)

# 4. clear the set using clear()
thisset.clear()
print(thisset)

# 5. delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # NameError: name 'thisset' is not defined

# The set() Constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)
