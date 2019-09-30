# Python Classes and Objects | Part 2

# Object Methods
# 1. Let us create a method in the Person class
# 2. Insert a function that prints a greeting
# and execute it on the p1 object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello! My name is", self.name)


p1 = Person("Nouf", 10)
p1.myfunc()
print("---------------------------")

# Modify Object Properties
# 3. Set the age of p1 to 40.
p1.age = 40
print(p1.age)
print("---------------------------")


# Delete Object Properties
# 4. Delete the age property from the p1 object.
del p1.age
# print(p1.age) # AttributeError: 'Person' object has no attribute 'age'

# Delete Objects
# 5. Delete the p1 object.
del p1
# print(p1) # NameError: name 'p1' is not defined
print("---------------------------")
