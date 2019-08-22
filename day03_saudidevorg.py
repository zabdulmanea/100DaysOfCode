# Python Variables

# Create str variable using double quotes
name = "Nouf"
print("The name is " + name)
# Create int variable
age = 9
print("The age is", age)

# Change the variable type from int to str
age = "Nine"
print("The age is " + age)

# Create str variable using single quotes
name = 'Nouf' # is the same name= "Nouf"
print(name)

# Create a variable starts with underscore "_"
_underscore = "Variable starts with _"
print(_underscore)

# Test the case sensitivity of the variables
CITY = "JEDDAH"
City = "Jeddah"
city = "jeddah"
print(CITY, City, city)

# Assign value to multiple variables in one line
city, region, country = "Jeddah", "Makkah", "Saudi Arabia"
print(city, region, country)

# Assign the same value to multiple variables in one line
food = fruit = red = "Apple"
print(food, fruit, red)

# Add a string variable to another string variable
print("Hello " + "World!")

# Add an int variable to another int variable
print(2+3)

# ---------- [Errors] ----------

# # Create a variable starts with number
# 2plus3 = 2

# # Create a variable contains an operator
# two+three = 3

# # Add a string variable to int variable
# print("Two is " + 2)
