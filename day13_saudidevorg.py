# Python Lists

# Declare an empty list
s = []
print(s)
print("---------------------------------------------")

# Declare a list contains only integer numbers
numbers = [1, 2, 3, 5, 8, 10]
print(numbers)
print("---------------------------------------------")

# Declare a list contains only strings
fruits = ["Apple", "Banana", "Cherry"]
print(fruits)
print("---------------------------------------------")

# Declare a list contains only decimal numbers
decimal_numbers = [1.23, 54.67, 123.98, 12.45]
print(decimal_numbers)
print("---------------------------------------------")

# Declare a list contains numbers & strings
this_list = [1, 2, 5, "Apple", "Orange", 6, "Lemon"]
print(this_list)
print("---------------------------------------------")

# Access list items
Apple = this_list[3]
print(Apple)
print("---------------------------------------------")

# Loop through a List
# Print all items in this_list
for item in this_list:
    print(item)
print("---------------------------------------------")

# Print all the numbers in the next list
num_list = [1, 4, 6, 12.54, 23.8, 23.5, 5]
for num in num_list:
    print(num)
print("---------------------------------------------")

# Change item value
# Change the third item from this_list
this_list[2] = "Cherry"
print(this_list)
print("---------------------------------------------")

# Delete item or list
# delete all the numbers items from this_list
del this_list[-2]
del this_list[1]
del this_list[0]
print(this_list)
print("---------------------------------------------")

# delete the list completely
del this_list
