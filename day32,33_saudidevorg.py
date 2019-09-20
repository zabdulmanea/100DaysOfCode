# Exercise

# create a list
def list_generator(start, end, step):
    numlist = []
    for x in range(start, end+1, step):
        numlist.append(x)
    return numlist

# print two lists
def print_lists(A, B):
    for x in A:
        for y in B:
            print(x, y)


# Lists
A = list_generator(3, 17, 2)  # odd list
B = list_generator(2, 16, 2)  # even list

# call the nested lists
print_lists(A, B)
