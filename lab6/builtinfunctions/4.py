from math import sqrt
from time import sleep
num = int(input())
ms = int(input())
sleep(ms / 1000) #turns sec into msec
sqr = sqrt(num)
print(f"The square root of {num} after {ms} miliseconds is {sqr}.")