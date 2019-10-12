# Week Challenges

# Challenge No. 1
import datetime
import calculator as cal

# First solution
print("1+8 = ", cal.calculate(1, 8, "+"))
print("4-2 = ", cal.calculate(4, 2, "-"))
print("6*6 = ", cal.calculate(6, 6, "*"))
print("8/2 = ", cal.calculate(8, 2, "/"))
print("---------------------------------------")

# Another Solution
print("1+8 = ", cal.add(1, 8))
print("4-2 = ", cal.sub(4, 2))
print("6*6 = ", cal.multiply(6, 6))
print("8/2 = ", cal.divide(8, 2))
print("---------------------------------------")

# Challenge No. 2
x = datetime.datetime.now()

print("- Time & Date of this Day:\n", x)
print("- Year:", x.year)
print("- Month:", x.month, "(", x.strftime("%B"), ")")
print("- Day:", x.day, "(", x.strftime("%A"), ")")
print("---------------------------------------")

# Challenge No. 3
print("Today date:", datetime.date.today())

tomorrow = datetime.date.today() + datetime.timedelta(days=1)
print("Tomorrow date:", tomorrow)

yesterday = datetime.date.today() - datetime.timedelta(days=1)
print("Yesterday date:", yesterday)
print("---------------------------------------")
