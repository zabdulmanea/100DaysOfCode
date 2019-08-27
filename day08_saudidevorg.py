# Python Strings - Part 2

# Removes whitespace from the beginning or the end of a string
name = "    Zinab      "
print("The name with spaces:", name)
print("The name after using strip():", name.strip())
print("---------------------------------------------")

# Get the length of a string
full_name = "Zinab Abdulmanea"
print("The length of", full_name, "is", len(full_name))
print("---------------------------------------------")

# Get the string in lower case
name = "SAUDI DEV ORG"
print("The name in Capital letters:", name)
print("Thae name after using lower()", name.lower())
print("---------------------------------------------")

# Get the string in upper case
name = "saudi dev org"
print("The name in Capital letters:", name)
print("Thae name after using upper()", name.upper())
print("---------------------------------------------")

# Replace a string with another string
x = "Code"
print("The original string:", x)
print("The string after replacement using replace():", x.replace('C', 'M'))
print("---------------------------------------------")

# Split the string into substrings
fruits = "Apple, Orange, Banana, Berry, Lemon"
print("The fruits list as one string:", fruits)
print("The fruits after spliting them into list:", fruits.split(', '))
print("---------------------------------------------")
