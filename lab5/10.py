import re  
#Write a Python program to convert a given camel case string to snake case. 
str = "camelCase"
pattern10 = r"(.)([A-Z].+)"
x1 = re.sub(pattern10, r"\1_\2", str)
print(x1.lower())