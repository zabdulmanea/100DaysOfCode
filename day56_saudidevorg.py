# Python JSON - PART 2

import json

x = {
    "name": "Ali",
    "age": 50,
    "married": True,
    "divorced": False,
    "Children": ("Mohammed", "Abdullah", "Ahmed"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# --- Format the result ---

# convert x into JSON then print the result
y = json.dumps(x, indent=4)
print(y)
print("---------------------------------------------")

z = json.dumps(x, indent=4, separators=(", ", " = "))
print(z)
print("---------------------------------------------")

# --- Order the result Alphabetically ---
w = json.dumps(x, indent=4, sort_keys=True)
print(w)
print("---------------------------------------------")
