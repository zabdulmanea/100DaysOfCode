# Python Regular Expressions - PART 1

# RegEx Module
import re

# Q: Search the string to see if
# it starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if(x):
    print("YES! We have a match!")
else:
    print("No match")

print("---------------------------------------------")

# ReqEx Functions
y = re.findall("in", txt)
print(y)
print("---------------------------------------------")

z = re.split(" in ", txt)
print(z)
print("---------------------------------------------")

w = re.sub("in", "at", txt)
print(w)
print("---------------------------------------------")

# Metacharacters
txt2 = "HHHHHHHHHHHHHH"
a = re.search("H+", txt2)
if(a):
    print("YES!")
else:
    print("NO!")
print("---------------------------------------------")

# Special Sequences
b = re.findall(r"\bin", txt)
print(b)
print("---------------------------------------------")

# Sets
c = re.findall("[arn]", txt)
print(len(c))
print("---------------------------------------------")
