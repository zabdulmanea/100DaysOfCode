# Day 18, 19

""" Exercise #1: Create a list and apply at least 4 methods on it """

# create a list contains three students: Nouf, Sara and Lujain
students = ["Nouf", "Sara", "Lujain"]
print("- Student names list:\n", students)

# add two new students to the list: Rawan and Nouf
students.append("Rawan")
students.insert(len(students), "Nouf")
print("- Students list after adding two new Students:\n", students)

# How many students have the name 'Nouf'?
num_nouf = students.count("Nouf")
print("- Number of students have the name 'Nouf':", num_nouf)

# Remove the last added student 'Nouf'
students.pop()
print("- Students list after deleting the last added student:\n", students)

# sort the students list alphabetically
students.sort()
print("- Students list ordered alphabetically:\n", students)
print("--------------------------------------------------------------")

""" Exercise #2: Create a tuple = ("java", "python", "swift")
    then check if it contains a 'python'? """

# create tuple
thistuple = ("java", "python", "swift")

# print the tuple
print("- The programming languages tuple is:")
print(thistuple)

# check the existence of 'python' in the tuple
# using 'in' keyword
print("- Does this tuple contains 'python'?", "python" in thistuple)

# check the existence of 'python' in the tuple
# using 'if-statement'
if "python" in thistuple:
    print("Yes, the tuple contains python")
else:
    print("No, the tuple doesn't contain python")

print("--------------------------------------------------------------")
