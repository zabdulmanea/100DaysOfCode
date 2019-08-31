# Day 12 - Text
text = "Please, I want {} sandwishes and {} donutes"
print("Before:\n", text)

# 1. Replace I with we
text = text.replace("I", "we")

# 2. Add 5, 7 sandwishes and dountes
num_sandwishes, num_donutes = 5, 7
text = text.format(num_sandwishes, num_donutes)

# 3. Convert any 'a' to 'A'
text = text.replace("a", "A", len(text))

# The output
print("After:\n", text)
