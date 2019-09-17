# Python Loops 2 - For Loop

# The For Loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("----------------------------")

# Looping Through a String
for letter in "apple":
    print(letter)
print("----------------------------")

# The break Statement
for letter in "apple":
    if letter == 'l':
        break
    print(letter)
print("----------------------------")

# The continue Statement
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
print("----------------------------")
