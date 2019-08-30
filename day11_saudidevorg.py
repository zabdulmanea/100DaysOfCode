# Python Operators - part 2

# Logical Operators
x = 5
print("Logical Operators (x = 5):")
print("(x < 6 or x > 7)?", x < 6 or x > 7)
print("(x < 6 and x > 7)?", x < 6 and x > 7)
print("not(x < 6)?", not(x < 6))
print("---------------------------------------------")

# Identity & Membership Operators
x = [1, 3]
y = [1, 3]
z = x
print(x is y)  # False
print(x is not y)  # True
print(x is not z)  # False
print(x != y)  # False
print(1 in x)  # True
print(3 not in x)  # False
print("---------------------------------------------")

# Bitwise Operators
# AND
print(15 & 3)  # 00001111 & 00000011 = 00000011 = 3
# XOR
print(3 ^ 3)  # 00000011 ^ 00000011 = 00000000 = 0
print("---------------------------------------------")
