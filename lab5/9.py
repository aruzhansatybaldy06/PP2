import re
# Write a Python program to insert spaces between words starting with capital letters.
str = "YouAreProgrammer"
pattern9 = r"(.)([A-Z])"
x = re.sub(pattern9, r"\1 \2", str)
print(x)