# Python Dictionaries - Part 1

# Create a Dictionary

# 1. create an empty dictionary
thisdict = {}
print(thisdict)

# 2. create a nonempty dictionary
thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": "1964"
}
print(thisdict)

# Accessing Items
# 1. access a value using []
model = thisdict["model"]
print(model)

# 2. access a value using get()
model = thisdict.get("model")
print(model)

# Change Values
thisdict["year"] = "2018"
print(thisdict)

# Loop Through a Dictionary

# 1. display the keys
for key in thisdict:
    print(key)

# 2. display the values using the keys
for key in thisdict:
    print(thisdict[key])

# 3. display the values using values() + for
for value in thisdict.values():
    print(value)

# 4. display the values using values()
print(thisdict.values())

# 5. display the keys & values using items() + for
for key, value in thisdict.items():
    print(key, value)

# 6. display the keys & values using items()
print(thisdict.items())
