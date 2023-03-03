import re
# Write a Python program to split a string at uppercase letters.
str = "Ad sdSDaaB45ghASdv"
pattern8 = r"[A-Z]+"
x = re.split(pattern8, str)
print(x)
