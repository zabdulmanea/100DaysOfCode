# Python JSON

import json

# --- Parse JSON – Convert from JSON to Python ---

# some JSON
JSONtext = '{ "name":"Jumanah", "age":10, "city":"Jeddah" }'

# parse JSON text:
parseJSON = json.loads(JSONtext)

# the result is a Python dictionary:
print(parseJSON["name"], ":",  parseJSON["age"])
print("---------------------------------------------")

# --- Convert from Python to JSON ---
# Python Objects: dict, list, tuple, string,
# int, float, true, false, none

# python object (dict):
thisdict = {
    "name": "Nouf",
    "age": 19,
    "city": "Taif"
}

# convert python dict into JSON:
JSONstring = json.dumps(thisdict)

# the result is a JSON string:
print(JSONstring)
print("---------------------------------------------")

# Q: Convert Python objects into JSON strings,
# and print the values:
print(json.dumps({"name": "Rawan", "age": 8}))  # dict
print(json.dumps(["Apple", "Orange"]))  # list
print(json.dumps(("Apple", "Cherry")))  # tuple
print(json.dumps("Hello!"))  # string
print(json.dumps(40))  # int
print(json.dumps(30.85))  # float
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print("---------------------------------------------")

# Q: Convert a Python object
# containing all the legal data types:

x = {
    "name": "Ali",
    "age": 50,
    "married": True,
    "divorced": False,
    "Children": ("Mohammed", "Abdullah", "Ahmed"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mbg": 27.5},
        {"model": "Ford Edge", "mbg": 24.1}
    ]
}
# convert into JSON then print the result
y = json.dumps(x)
print(y)
print("---------------------------------------------")
