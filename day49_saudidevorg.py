# Python Scope - Part 2


x = 500  # Global Variable
w = 600


def myfunc():
    x = 300  # Local Variable
    print(x)

    global y  # Global Variable
    y = 200

    z = 100  # Local Variable

    global w
    w = 400
    print(w)


myfunc()
print(x)
print(y)
# print(z)  # NameError: name 'z' is not defined
print(w)
