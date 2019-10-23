# Python Try-Except
"""
Try block: test a block of code for errors.
Except block: handle the error.
Finally block: execute code, regardless of 
the result of the try- and except blocks.
"""

# 1. Exception Handling
try:
    print(x)
except:
    print("An exception occurred")
print("-------------------------")

# Error: NameError: name 'x' is not defined
# print(x)

# 2. Many Exceptions

# Q: print one message if the try block raises
# a NameError and another for other errors.
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
print("-------------------------")

# 3. Else
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
print("-------------------------")

# 4. Finally
try:
    print(x)
except:
    print("Something went wrong")
else:
    print("The 'try except' is finished")
print("-------------------------")
