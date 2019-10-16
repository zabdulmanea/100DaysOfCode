# Python Regular Expressions - PART 2
import re

# The findall() Function
# Q: Print a list of all matches of "ai"

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
print("--------------------------------------")

y = re.findall("Jeddah", txt)
print(y)
if(y):
    print("Yes, there is at least one match!")
else:
    print("No match!")
print("--------------------------------------")

# The search() Function
# Q: Search for the first white-space character in the string.
z = re.search(r"\s", txt)
print("The first white-space is located in position:", z.start())
print("--------------------------------------")

# Q: Make a search that returns no match:
w = re.search("Jeddah", txt)
print(w)
print("--------------------------------------")

# The Split() Function
# Q: Split at each white-space character:
n = re.split(r"\s", txt)
print(n)
print("--------------------------------------")
