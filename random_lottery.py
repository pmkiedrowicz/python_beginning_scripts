'''
Lottery game –  Generate a 100 Lottery tickets and pick two lucky tickets from it as a winner.
Lottery number must be 10 digits long.
'''
import random

i = 0
ls = []
while i < 100:
    val = random.randrange(1000000000, 9999999999)
    ls.append(val)
    i += 1

final_list = random.sample(ls, 2)
print(final_list)
