# Python String Formatting - PART 1

# String format()

# Q: Add a placeholder where you want to display the price.
price = 50
txt = "The price is {} dollars"
print(txt.format(price))

# Q: Format the price to be displayed as a number with two decimals.
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple Values
quantity = 5
itemno = 678
price = 67
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
