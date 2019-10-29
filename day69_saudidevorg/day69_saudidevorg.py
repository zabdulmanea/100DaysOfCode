# File Handling

import os

# 1. Python File Read

# Open a File on the Server
f = open("day69_saudidevorg/demofile1.txt")
f.close()
# or
f = open("day69_saudidevorg/demofile1.txt", "rt")  # read text
f.close()
# or
f = open("day69_saudidevorg/demofile1.txt", "r")  # read

print(f.read())
f.close()
print("-----------------------------")

# Read Only Parts of the File
# Q: Return the 5 first characters of the file
f = open("day69_saudidevorg/demofile1.txt")
print(f.read(5))
f.close()
print("-----------------------------")

# Read Lines
# Q: Read two line of the file.
f = open("day69_saudidevorg/demofile1.txt")
print(f.readline())
print(f.readline())
f.close()
print("-----------------------------")

# Q: Loop through the file line by line.
f = open("day69_saudidevorg/demofile1.txt")
for i in f:
    print(i)
f.close()
print("-----------------------------")

# 2. Python File Write

# Write to an Existing File
# Q: Open the file "demofile2.txt" and append content to the file.
f = open("day69_saudidevorg/demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("day69_saudidevorg/demofile2.txt", "r")
print(f.read())
f.close()
print("-----------------------------")

# Q: Open the file "demofile3.txt" and overwrite the content.
f = open("day69_saudidevorg/demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
print("-----------------------------")

f = open("day69_saudidevorg/demofile3.txt", "r")
print(f.read())
f.close()
print("-----------------------------")

# 3. Create a New File

# Q: Create a file called "myfile1.txt".
if not os.path.exists("day69_saudidevorg/myfile1.txt"):
    f = open("day69_saudidevorg/myfile1.txt", "x")
    print("'myfile1.txt' has been created!")
f.close()
print("-----------------------------")

# 4. Delete a File

# Q: Create a new file if it does not exist,
# and delete it if it exists.

if os.path.exists("day69_saudidevorg/mydemo.txt"):
    os.remove("day69_saudidevorg/mydemo.txt")
    print("'mydemo.txt' has been deleted!")
else:
    f = open("day69_saudidevorg/mydemo.txt", "w")
    print("'mydemo.txt' has been created!")
    f.close()
print("-----------------------------")

os.remove("day69_saudidevorg/myfile1.txt")
print("'myfile1.txt' has been deleted!")
print("-----------------------------")

# 5. Delete Folder
if not os.path.exists("day69_saudidevorg/myfolder"):
    os.makedirs("day69_saudidevorg/myfolder")
os.rmdir("day69_saudidevorg/myfolder")
print("'myfolder' has been deleted!")
print("-----------------------------")
