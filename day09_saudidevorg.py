# String Format

# Combine strings and numbers
age = 10
txt = "My name is Nouf, and I'm {}"  # one argument
print(txt.format(age))
print("---------------------------------------------")

# multiple arguments
quantity = 5
item_id = 370
price = 99.75
order = "I want {} pieces of item no. {} for {} SR"
print(order.format(quantity, item_id, price))
print("---------------------------------------------")

# use index numbers to every arguments
order = "I want to pay {2} SR for {0} pieces of item no. {1}"
print(order.format(quantity, item_id, price))
print("---------------------------------------------")
