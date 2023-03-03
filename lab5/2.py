import re
# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
str = "abbb"
pattern2 = r"ab{2,3}"
x = re.search(pattern2, str)
if x: 
    print("A match is found!")
else:
    print("Not matched!")
