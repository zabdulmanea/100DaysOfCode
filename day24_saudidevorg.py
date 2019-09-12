# Python Dictionaries - Part 3

# Create a Dictionary
thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": "1964"
}
print(thisdict)

# Copy a Dictionary

# 1. copy a dictionary using the built-in method copy()
mydict = thisdict.copy()
print(mydict)

# 2. copy a dictionary using the built-in method dict()
mydict = dict(thisdict)

# Nested Dictionaries
# 1. a dictionary that contain three dictionaries
myfamily = {
    "child1": {
        "name": "Mohammed",
        "year": "1990"
    },
    "child2": {
        "name": "Abdullah",
        "year": "1992"
    },
    "child3": {
        "name": "Ahmed",
        "year": "1999"
    }
}
print(myfamily)

# 2. one dictionary contains a three existing dictionaries
child1 = {
    "name": "Mohammed",
    "year": "1990"
}
child2 = {
    "name": "Abdullah",
    "year": "1992"
}
child3 = {
    "name": "Ahmed",
    "year": "1999"
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)

# make a new dictionary using dict() Constructor
thisdict = dict(brand="ford", model="Mustang", year="1964")
print(thisdict)
