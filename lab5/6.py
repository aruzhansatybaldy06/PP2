import re
# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
str = "asdf hf. kj,"
pattern6 = r"[\s,.]"
x = re.sub(pattern6, ":", str)
print(x)