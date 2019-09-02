# Python Lists - part 2

# Access part of list
thislist = ["A", "B", "C", "D", "E"]
print(thislist[1:3])  # ["B","C"]
print("---------------------------------------------")

# print the elements from "C" to "E" as a list
print(thislist[2:])
print("---------------------------------------------")

# Check if item exists
thislist = ["Apple", "Banana", "Cherry"]
if "Apple" in thislist:
    print("Yes, Apple is in the fruits list")
print("---------------------------------------------")

# Repeat item in list
thislist3 = thislist * 3
print(thislist3)
print("---------------------------------------------")

# + operator in list
sisterslist = ["Sara", "Maha", "Lujain"]
brotherslist = ["Ahmed", "Khalid", "Salem"]
siblinglist = sisterslist + brotherslist
print(siblinglist)
print("---------------------------------------------")

intlist = [3, 4, 7, 1, 9]
floatlist = [34.6, 45.9, 2.4, 17.89, 99.2]
numberslist = intlist + floatlist
print(numberslist)
print("---------------------------------------------")
