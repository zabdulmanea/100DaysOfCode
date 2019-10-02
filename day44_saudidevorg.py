# Python Inheritance | Part 2

# 1. Use the super() Function
# 2: Add a property called graduationyear to the Student class
# 3. Add a year parameter, and pass the correct year when creating objects.
# 4. Add a method called welcome to the Student class.


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("Hello, my name is",
              self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname) # 1
        # self.graduationyear = 2019 # 2
        self.graduationyear = year # 3
    # 4
    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)


x = Student("Rawan", "Ahmed", 2015)
x.printname()
print(x.graduationyear)
x.welcome()
print("--------------------------------")
