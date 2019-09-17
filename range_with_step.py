'''
Generate 3 random integers between 100 and 999 which is divisible by 5.
'''
import random

i = 0
ls = []
while i < 3:
    val = random.randrange(100, 999, 5)
    ls.append(val)
    i += 1
print(ls)
