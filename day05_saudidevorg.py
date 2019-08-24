# basket = x + y + z
# x= apple , y = orange , z= limon

# define the fruites
x, y, z = "apple", "orange", "limon"

# assign the fruit to the basket
basket = x + y + z

# print the basket
print("The basket fruits before spliting them:")
print(basket)

# Determine the length of each fruit
x_len = len(x)
y_len = len(y)
z_len = len(z)

# print the basket in formatted way using substring and fruits length
print("The basket fruits in formatted way using length and substring functions:")
print(basket[:x_len], basket[x_len:y_len+x_len], basket[-1*z_len:])
