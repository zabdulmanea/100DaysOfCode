# Python Regular Expressions - PART 3
import re

# The sub() Function
# Q: Replace every white-space character with the number 9.

txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt)
print(x)

# Q: Replace the first 2 occurrences of the white speace with number 9
y = re.sub(" ", "9", txt, 2)
print(y)
print("--------------------------------------")

# Match Object
# Q: Do a search that will return a Match Object.
z = re.search("ai", txt)
print(z)

# Q: Print the position (start- and end-position) of the first match occurrence.
w = re.search(r"\bS\w+", txt)
print(w)
print(w.span())

# Q: Print the string passed into the function.
print(w.string)

# Q: Print the part of the string where there was a match.
print(w.group())

print("--------------------------------------")
