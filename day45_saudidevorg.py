# Python Iterators

# Iterator vs Iterable
# 1. Return an iterator from a tuple, and print each value.
mytuple = ("apple", "banana", "cherry")  # iterable
myit = iter(mytuple)  # iterator

[print(next(myit)) for x in mytuple]
print("--------------------------------")


# 2. Return an iterator from a string, and print each value.

mystr = "apple"
myit = iter(mystr)

[print(next(myit)) for x in mystr]
print("--------------------------------")


# Looping Through an Iterator
[print(x) for x in mytuple]
print("--------------------------------")

[print(x) for x in mystr]
print("--------------------------------")

# Create an Iterator
# 3. Create an iterator that returns numbers, starting with 1,
# and each sequence will increase by one (returning 1,2,3,4,5 etc.)
# 4. Stop after 20 iterations.


class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = Mynumbers()
myiter = iter(myclass)

[print(x) for x in myiter]
print("--------------------------------")
