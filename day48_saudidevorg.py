# Python Scope - Part 1

y = 500  # 3. variable with global scope


def myfunc():
    x = 300  # 1. variable with local scope
    print(x)
    print(y)
    # 2. Function Inside Function

    def myinnerfunc():
        print(x)

    myinnerfunc()

# 3. Global Scope


myfunc()
print(y)
print("--------------------------------")
