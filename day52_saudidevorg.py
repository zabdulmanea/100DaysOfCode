# Python Datetime

# Q: Import the datetime module
import datetime

# Q: Display the current date
x = datetime.datetime.now()
print(x)

# Q: Return the year and name of weekday
print(x.year)
print(x.strftime("%A"))  # takes one parameter, format.

# Q: Create a date object
y = datetime.datetime(2020, 10, 5)
print(y)

# Q: Display the name of the month
print(y.strftime("%B"))
