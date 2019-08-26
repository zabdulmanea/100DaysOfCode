# Python Strings - Part 1

# Print 'Hello' (surrounded by single quotation marks) 
print('Hello')
# Print "Hello" (surrounded by double quotation marks)
print("Hello")
print("---------------------------------------------")

# Assign string to a variable
name = "Zinab"
print("Name:", name)
print("---------------------------------------------")

# Write multiline string 
multiline_text = """ A multiline string in Python 
begins and ends with either three single quotes 
or three double quotes. Any quotes, tabs, or newlines 
in between the “triple quotes” are considered part of 
the string. Python’s indentation rules for blocks do not 
apply to lines inside a multiline string. """
print(multiline_text)
print("---------------------------------------------")

# Strings are Arrays

# Print character 'L' in "ZINAB ALI"
name = "ZINAB ALI"
print("Print character 'L' in 'ZINAB ALI':")
print(name[7])

# Get the forth character in "ZINAB ALI"
print("Print the 4th character in 'ZINAB ALI':")
print(name[3])

# Get the second name of "ZINAB ALI"
print("Print the second name of 'ZINAB ALI':")
print(name[6:9])
print(name[6:])
print(name[-3:])
print("---------------------------------------------")
