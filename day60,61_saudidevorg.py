# Week 9 Challenges
import json
import re

print("\n\n-------------- Challenge 1: JSON --------------")

weekdays = ("Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat")
JSONdays = json.dumps(weekdays)
print(JSONdays)
print(type(JSONdays))

print("\n\n-------------- Challenge 2: RegEx --------------")

txt = "data is the new oil"
data = re.search("data", txt)
if (data):
    print("YES! data is located in position:", data.span())
else:
    print("No! There is no match.")

print("\n\n----------- Challenge 3: RegEx & JSON -----------")

python = {
    "name": "Python Programming Language",
    "current-version": "3.7.4",
    "properties":
    ("interpreted", "object-oriented", "high-level"),
    "uses": [
        "Web Development", "Artificial Intelligence",
        "data Analysis", "Machine Learning", "Game Development"
    ],
    "dynamically type": True,
}

pythonString = json.dumps(python, indent=4)
print(pythonString)
print("----------------------------------------------")

# Q: Find the "current-version" of python
currentversion = re.search(r'current-version.*([0-9]+.)+', pythonString)

if (currentversion):
    serachresult = currentversion.group()
    version_num = re.search(r'((\d)+.)+\d+', serachresult)

    print("The current version of python is", version_num.group())
else:
    print("There is no Version found!")
print("----------------------------------------------")

# Change ":" to "="
pythonString = re.sub(r":", "=", pythonString)
print(pythonString)
