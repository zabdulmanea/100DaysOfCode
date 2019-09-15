# Conditional Statements if ... else

# 1. If statements
a = 330
b = 20
if a > b:
    print("a is greater than b")

# ERROR: without indentation
# if a > b:
# print("a is greater than b")
# # IndentationError: expected an indented block

# 2. if ... else if
a = 30
b = 30
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")

# 3. if ... elif ... else
a = 30
b = 50
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("a is smaller than b")

# 4. if ... else
if a > b:
    print("a is greater than b")
else:
    print("a is smaller than b")

# 1. Short Hand If
if b > a:
    print("b is greater than a")

# 2. Short Hand If ... Else
# a. one else
print("A") if a > b else print("B")
# b. multiple else
print("A") if a > b else print("=") if a == b else print("B")

# And
# Test if a is smaller than b, AND if c is greater than a
a = 20
b = 50
c = 30
if a < b and c > a:
    print("Both conditions are True")

# Or
# Test if a is greater than b, OR if a is greater than c
a = 30
b = 50
c = 20
if a > b or a > c:
    print("At least one condition is True")

# Nested If
x = 15
if x > 10:
    print("x is above 10, ")
    if x > 20:
        print("and x is above 20!")
    else:
        print("and x is not above 20!")
