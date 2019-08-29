# Python Operators - part 1

# Arithmetic Operators
x = 5
y = 3

print("x =", x, "\ny =", y)
print("x * y =", x * y)  # 5x3 = 15
print("x / y =", x / y)  # 5/3 = 1.67
print("x + y =", x + y)  # 5+3 = 8
print("x - y =", x - y)  # 5-3 = 2
print("x % y =", x % y)  # remainder of 5/3 = 3
print("x ** y =", x ** y)  # 5 to the power of 3 = 125
print("x // y =", x // y)  # 5//3 = 1 (without decimal part)
print("---------------------------------------------")

# Assignment Operators
z = 15
print("z =", z)

z /= 3  # z = z / 3 = 5.0
print("z = z / 3 =", z)

z += 3  # z = z + 3 = 5 + 3 = 8.0
print("z = z + 3 =", z)

# ---- (Bitwise) ----
w = 15
print("w =", w)

w &= 3  # w = w & 3 (AND)
# w = 00001111 & 00000011 = 00000011 = 3
print("w = w & 3 =", w)

w ^= 3  # w = w ^ 3 (XOR)
# 00000011 ^ 00000011 = 00000000 = 0
print("w = w ^ 3 =", w)
print("---------------------------------------------")

# Comparison Operators
x = 15
y = 30

txt = "Is {} {} {} ?"

operator = "equals"
print(txt.format(x, operator, y), x == y)

operator = "does not equals"
print(txt.format(x, operator, y), x != y)

operator = "greater than"
print(txt.format(x, operator, y), x > y)

operator = "smaller than"
print(txt.format(x, operator, y), x < y)

operator = "greater than or equals to"
print(txt.format(x, operator, y), x >= y)

operator = "smaller than or equals to"
print(txt.format(x, operator, y), x <= y)
print("---------------------------------------------")
