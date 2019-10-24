# Python String Formatting - PART 2

# Index Numbers
quantity = 3
itemno = 468
price = 899
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 56
name = "Ali"
txt = "His name is {0}. {0} is {1} years old."
print(txt.format(name, age))

# Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
