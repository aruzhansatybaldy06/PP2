import re
# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
str = "abbbbut"
pattern1 = r"ab*"
x = re.search(pattern1, str)
if x: 
    print("A match is found!")
else:
    print("Not matched!")
