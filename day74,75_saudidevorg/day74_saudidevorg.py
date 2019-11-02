"""
Week 11 : Challenge 1
        : Extra Challenge
"""

# ---------- Challenge 1 -------------


def readtext():
    f = open("day74,75_saudidevorg/python.txt")
    print(f.read())
    f.close()
    print("-----------------------------------")


# 1. Read the file
readtext()

# 2. Append new text to the file then read it
f = open("day74,75_saudidevorg/python.txt", "a")
f.write("\nThe best way we learn anything is by practice and exercise questions.")
f.close()
print("-----------------------------------")
# read the file
readtext()

# ---------- Extra Challenge -------------

f = open("day74,75_saudidevorg/python.txt")
filelist = f.readlines()
for line in filelist:
    print(line)
f.close()
print("-----------------------------------")
