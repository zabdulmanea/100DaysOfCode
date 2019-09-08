# Python Sets

# Set {}
# 1. create an empty set
thisset = {}
print("- An empty list:", thisset)
print("---------------------------------------------")

# 2. create a set
# sets contain unordered items
fruits_set = {"apple", "banana", "cherry"}
print("- Fruits set:", fruits_set)
print("---------------------------------------------")

# 3. create a set contains repeated items
# sets contain only unique items
thisset = {1, 1, 5, 7, "Reem", 7, "Reem"}
print("- A set contains repeated items:\n", thisset)


# Access Items
# there is no index because sets are unordered

# 1. Loop through the set and print the values
print("- The set items:")
for item in thisset:
    print(item)

# 2. Check if "Reem" is present in the set.
print("- Does the set contains 'Reem'?", "Reem" in thisset)

# Change Items
#  we cannot change sets' items

# Add Items
# 1.  add one item to a set
thisset.add("Rawan")
print("- The set after adding 1 item using add():\n", thisset)

# 2. add more than one item to a set
thisset.update(["Sara", "Maha", "Nouf"])
print("- The set after adding multiple items using update():\n", thisset)
print("---------------------------------------------")
