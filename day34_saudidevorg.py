# Python Function - Part 2

# Passing a List as a Parameter
def food_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "orange"]
food_function(fruits)
print("----------------------------")

# Return Values
def my_function1(x):
    return 5 * x

print(my_function1(2))
print("----------------------------")

# Keyword Arguments = kwargs
def children1(child3, child1, child2):
    print("The youngest child is:", child3)

children1(child1="Mohammed", child2="Abdullah", child3="Ahmed")
print("----------------------------")

# Arbitrary Arguments
def children2(*kids):
    print("The youngest child is:", kids[2])

children2("Mohammed", "Abdullah", "Ahmed")
print("----------------------------")

# Recursion
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results")
tri_recursion(6)
print("----------------------------")
