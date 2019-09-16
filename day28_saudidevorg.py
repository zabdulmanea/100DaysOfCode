# Python Loops 1 - While Loop

# The while Loop
# Print i as long as i is less than 6
i = 1
while i < 6:
    print(i)
    i += 1
print("----------------------------")

# The break Statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("----------------------------")

# The continue Statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("----------------------------")

# The else Statement
i = 10
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer than 6!")
print("----------------------------")
