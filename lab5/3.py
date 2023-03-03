import re
# Write a Python program to find sequences of lowercase letters joined with a underscore.
str = "hk_jnnh"
pattern3 = r"^[a-z]+_[a-z]+$"
x = re.findall(pattern3, str)
if x: 
    print(x)
    print("A match is found!")
else:
    print("Not matched!")
