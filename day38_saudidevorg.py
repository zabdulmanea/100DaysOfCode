# Python Arrays - part 2

# Create an array containing car names
cars = ["Ford", "Volvo", "BMW"]
print(cars)
print("---------------------------")

# Looping Array Elements
for car in cars:
    print(car)
print("---------------------------")

# Adding Array Elements
cars.append("Honda")
print(cars)
print("---------------------------")

# Removing Array Elements
# 1. use pop to delete an item by index
cars.pop(1)
print(cars)
print("---------------------------")
# 2. use remove to delete an item by name
cars.remove("BMW")
print(cars)
print("---------------------------")

# Array Methods
cars.reverse()
print(cars)
print("---------------------------")
