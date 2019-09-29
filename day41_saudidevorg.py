# Python Classes and Objects | Part 1

# 1. Create a class named MyClass, with a property named x.
class MyClass:
    x = 5


print(MyClass)
print("---------------------------")

# 2. Create an object named p, and print the value of x.
p = MyClass()
print(p.x)
print("---------------------------")

# 3. The __init__() Function & the self Parameter
# Create a class named Person,
# use the __init__() function to assign values for name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello! My name is", self.name)


p1 = Person("Nouf", 10)
print(p1.name)
print(p1.age)
p1.myfunc()
print("---------------------------")


# 4. Create a class then
# use the words mysillyobject and abc instead of self.
class Food:
    def __init__(mysillyobject, name, category):
        mysillyobject.name = name
        mysillyobject.category = category

    def myfunc(abc):
        print("The", abc.name, "category is", abc.category)


food1 = Food("Apple", "Fruit")
print(food1.name, ":", food1.category)
food1.myfunc()
print("---------------------------")
