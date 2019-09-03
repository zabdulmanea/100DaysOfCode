# Python Lists - part 3

# List Methods
thislist = ["Apple", "Banana", "Cherry"]
print("The list is:\n", thislist)
print("---------------------------------------------")

# List Length
print("The list length = ", str(len(thislist)))
print("---------------------------------------------")

# Add Items
# 1. add an item at the end of the list
print("Adding 'Orange' at the end of the list:")
thislist.append("Orange")
print(thislist)
print("---------------------------------------------")

# 2. add an item at the specified index
print("Adding 'Lemon' between banana and cherry:")
thislist.insert(2, "Lemon")
print(thislist)
print("---------------------------------------------")

# add an existing item at the end of the list
print("Adding 'Banana' at the end of the list:")
thislist.append("Banana")
print(thislist)
print("---------------------------------------------")

# Remove Item
# 1. a. Remove specified item from the list
print("Removing 'Banana' from the list:")
thislist.remove("Banana")  # the first banan will be removed
print(thislist)
print("---------------------------------------------")

# b. Remove specified item from the list
print("Removing 'Lemon' from the list:")
thislist.pop(1)  # item in index 1 will be removed
print(thislist)
print("---------------------------------------------")

# 2. Remove the last item from the list
print("Removing the last item from the list:")
thislist.pop()
print(thislist)
print("---------------------------------------------")

# Copy a List
# Way 1 to copy list
mylist = thislist.copy()
print("A copy of the list using copy(): ", mylist)
print("---------------------------------------------")

# Way 2 to copy list
mylist2 = list(thislist)
print("A copy of the list using list(): ", mylist2)
print("---------------------------------------------")

# Clear a List
print("Clear the list (Delete all items without deleting the list):")
thislist.clear()
print(thislist)
print("---------------------------------------------")

#  Make a new list
thislist = list(("Apple", "Banana", "Cherry"))
print("List created using list() method:")
print(thislist)
print("---------------------------------------------")

# Count Method
thislist.append("Banana")
print(thislist)
print("Number of Bananas = ", thislist.count("Banana"))

# Reverse List
thislist.reverse()
print("The list from right to left:\n", thislist)

# Sort list
thislist.sort()
print("Order the list alphabetically:\n", thislist)
print("---------------------------------------------")
