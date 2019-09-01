# Day 12
import re

text = "Please, I want {} sandwishes and {} donutes"
print("Before:\n", text)

# 1. Replace I with we
text = text.replace("I", "we")

# 2. Add 5, 7 sandwishes and dountes
num_sandwishes, num_donutes = 5, 7
text = text.format(num_sandwishes, num_donutes)

# 3. Convert any 'a' to 'A'
# text = text.replace("a", "A")

# 3. Another way to convert each 'a' to 'A'
# Uses the regular expression engine to
# find any 'a' and replace it with 'A'
letter = 'a'
text = re.sub(letter, letter.upper(), text)

# The output
print("After:\n", text)
