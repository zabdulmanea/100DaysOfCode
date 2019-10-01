# Python Inheritance | Part 1

# Create a Parent Class
# Q: Create a class named Person, with firstname
# and lastname properties, and a printname method.
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("Hello, my name is",
              self.firstname, self.lastname)


x = Person("Nouf", "Mohammed")
x.printname()
print("--------------------------------")

# Create a Child Class
# Q: Create a class named Student, which will inherit
# the properties and methods from the Person class.
class Student(Person):
    # pass: there is no new properties or methods in the class.
    pass


y = Student("Rawan", "Ahmed")
y.printname()
print("--------------------------------")

# Add the __init__() Function
class Employee(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


z = Employee("Jumanah", "Abdullah")
z.printname()
print("--------------------------------")
