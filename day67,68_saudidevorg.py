# Week 10 challenge

""" Challenge 1: Command Line Input  """

print("Enter the first letter of your name:")
fletter = input()
print("Enter the last letter of your name:")
lletter = input()

name = "Your name starts with {} and ends with {}."

print(name.format(fletter[0], lletter[0]))
print("------------------------------")

""" Challenge 2: String Formatting  """
fname = "Ahmad"
lname = "Ali"
balance = 35.44

txt = "Dear {} {}, Your current balance is {:.2f} $"
print(txt.format(fname, lname, balance))
print("------------------------------")

""" Challenge 3  """
print("Enter number of elements:")
elements_num = input()
elements = []
for i in range(0, int(elements_num)):
    print("Enter the value of index no. {}:".format(i))
    elements.append(input())

print(elements)
print("------------------------------")
