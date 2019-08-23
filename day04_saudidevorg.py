import random

# Python Numbers

# Numeric variables types 
x = 2 # integer number
y = 2.5 # float number
z = 2j # complex number

# Print the numbers and determine their types
print("Print the numbers and determine their types")
print(x, ":", type(x))
print(y, ":", type(y))
print(z, ":", type(z))
print("----------------------------------------")

# Integer numbers
positive_int = 2 # positive integer
negative_int = -2 # negative integer
long_int = 245565768798779789 # long integer

# Print the integer numbers and determine their types
print("Print the integer numbers and determine their types")
print(positive_int, ":", type(positive_int))
print(negative_int, ":", type(negative_int))
print(long_int, ":", type(long_int))
print("----------------------------------------")

# Float numbers
positive_float = 2.56 # positive float
negative_float = -25.367 # negative float
powerOf10_float = -82.56e100 # scientific numbers with an "e"

# Print the float numbers and determine their types
print("Print the float numbers and determine their types")
print(positive_float, ":", type(positive_float))
print(negative_float, ":", type(negative_float))
print(powerOf10_float, ":", type(powerOf10_float))
print("----------------------------------------")

# Complex numbers
x = 3+5j
y = 5j
z = -5j

# Print the complex numbers and determine their types
print("Print the complex numbers and determine their types")
print(x, ":", type(x))
print(y, ":", type(y))
print(z, ":", type(z))
print("----------------------------------------")

# Type Conversion

x = 1 # int
y = 2.5 # float
z = 2j # complex

# convert from integer to float
a = float(x)
# convert from integer to complex
b = complex(x)
# convert from float to complex
c = complex(y)
# convert from float to int
d = int(y)

# Print the numbers and their types
print("Convert the int number", x , "to float:")
print(a, ":", type(a))
print("Convert the int number", x , "to complex:")
print(b, ":", type(b))
print("Convert the float number", y , "to complex:")
print(c, ":", type(c))
print("Convert the float number", y , "to int:")
print(d, ":", type(d))
print("----------------------------------------")


#  Display a random number between 1 and 100
print("Random number between 1 and 100:")
print(random.randrange(1,101))

# ------------ [Errors] ------------
# # convert from complex to float
# d = float(z)
# # convert from complex to int
# e = int(z)
