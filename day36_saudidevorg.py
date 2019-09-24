# Python Lambda - part 2

# Why Use Lambda Functions?

# a function that takes one argument, and that
# argument will be multiplied with an unknown number

def myfunc(n):
    return lambda a: a * n


# make a function that always doubles a number
mydoubler = myfunc(2)
print(mydoubler(11))

# def mydoubler(a):
#     return a * 2

# make a function that always triple a number
mytripler = myfunc(3)
print(mytripler(11))
