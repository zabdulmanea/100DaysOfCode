# Python Modules - Part 2

# Re-naming a Module
import mymodule as mx

# Built-in Modules
# Q: Import and use the platform module.
import platform

# Import From Module
# Q: Import only the person1 dictionary from mymodule.
from mymodule import person

# Use mymodule module
print(mx.person["name"])
print("----------------------------")

# Use Built-in Modules (platform)
print(platform.system())
print(platform.python_version)
print("----------------------------")

# Using the dir() Function
# Q: List all the defined names in platform module.
print(dir(platform))
print("----------------------------")

# Q: List all the defined names belonging to mymodule.
print(dir(mx))
print("----------------------------")

# Use person dict from mymodule
print(person["name"])
print("----------------------------")
