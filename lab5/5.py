import re
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
str = "afb1 3b"
pattern5 = r"^a.+b$"
x = re.search(pattern5, str)
if x: 
    print("A match is found!")
else:
    print("Not matched!")
