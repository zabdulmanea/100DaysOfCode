# Python Dictionaries - Part 2

# Create a Dictionary
thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": "1964"
}
print(thisdict)

# Check if Key Exists
if "model" in thisdict:
    print("Yes, 'model' is a key in thisdict dictionary")

# Dictionary Length
print(len(thisdict))

# Adding Items
thisdict["color"] = "Black"
print(thisdict)

# Removing Items

# 1. remove the item 'key-value pair' using pop()
thisdict.pop("model")
print(thisdict)

# error: remove a non-exist item using pop()
# thisdict.pop("price") # KeyError: 'price'

# 2. remove the last inserted item using popitem()
thisdict.popitem()
print(thisdict)

# error: remove an item from empty dictionary
thisdict = {}
# thisdict.popitem() # KeyError: 'popitem(): dictionary is empty'

thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": "1964"
}

# 3. remove the item 'key-value pair' using del
del thisdict["model"]
print(thisdict)

# 4. clear the dictionary
thisdict.clear()
print(thisdict)

# 5. delete the dictionary completely
del thisdict
# print(thisdict) # NameError: name 'thisdict' is not defined
