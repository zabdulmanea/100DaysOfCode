# Python Loops 3 - For Loop

# The range() Function
# 1. x starts from 0 to 5 and increases by 1
for x in range(6):
    print(x)
print("----------------------------")

# 2. x starts from 2 to 5 and increases by 1
for x in range(2, 6):
    print(x)
print("----------------------------")

# 3. x starts from 3 to 30 and increases by 3
for x in range(3, 31, 3):
    print(x)
print("----------------------------")

# Else in For Loop
for x in range(4):
    print(x)
else:
    print("Finally Finished!")
print("----------------------------")

# Nested Loops
adjs = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for adj in adjs:
    for fruit in fruits:
        print(adj, fruit)
print("----------------------------")
