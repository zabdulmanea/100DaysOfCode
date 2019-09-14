# Day 25, 26

""" Exercise #1: Add these numbers 4,8,12 to set={1,3,5,7,8}
then delete number 8, and finally clear the set
"""
# the set
thisset = {1, 3, 5, 7, 8}
print(thisset)

# add 4,8,12 to the set
thisset.update([4, 8, 12])
print(thisset)

# remove number 8 from the set
thisset.remove(8)
print(thisset)

# clear the set
thisset.clear()
print(thisset)
print("---------------------------------------------")

""" Exercise #2: create a dictionary
and add {name: pigeon, type: bird, skin cover: feathers}
then print the value of type,
then change the value of skin cover
"""

# create a dictionary
thisdict = {
    "name": "pigeon",
    "type": "bird",
    "skin cover": "feathers"
}
print(thisdict)

# print the value of "type"
print(thisdict["type"])

# change the "skin cover" value
thisdict["skin cover"] = "plume"
print(thisdict)
print("---------------------------------------------")
