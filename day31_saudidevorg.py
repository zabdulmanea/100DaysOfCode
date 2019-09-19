# Python Functions

# a. Built-in Function: 
# like print() - len() - range()

# b. User-Defined Functions

# Creating a Function

# 1. without parameters
def myFunction1():
    print("Hello, this is a function!")

# 2. one parameter
def myFunction2(name):
    print("Hello", name, "!")

# 3. default parameter value
def myFunction3(city="Jeddah"):
    print("Hello, I live in", city, "!")


# Calling Functions
myFunction1()

myFunction2("Zinab")
myFunction2("Daniah")

myFunction3()
myFunction3("Taif")
myFunction3("Makkah")
