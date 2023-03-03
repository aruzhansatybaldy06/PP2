import re
# Write a python program to convert snake case string to camel case string.
str = "snake_case"
#убирает нижние пробелы превращая в список, затем перепиcывает их с заглавной буквы и объединяет обратно
pattern7 = "".join(x.capitalize() or "_" for x in str.split("_"))
print(pattern7)
