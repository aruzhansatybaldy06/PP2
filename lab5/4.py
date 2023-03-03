import re
# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
str = "Python"
pattern3 = r"[A-Z][a-z]+"
x = re.findall(pattern3, str)
if x: 
    print(x)
    print("A match is found!")
else:
    print("Not matched!")