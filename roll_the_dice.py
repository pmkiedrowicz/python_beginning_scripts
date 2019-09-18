'''
Roll dice in such a way that every time you get the same number
Dice has 6 number(from 1 to 6). Roll dice in such a way that every time you must get same output number. do this 5 times.
'''

import random
from datetime import datetime


def roll():
    return random.randrange(1, 6)


def get_time():
    return datetime.now()


def time_difference(before, after):
    return (after - before).seconds


i = 0
j = 0
j = roll()
k = 0
before_time = get_time()
while i < 5:
    k += 1
    if roll() == j:
        i += 1
    else:
        i = 0
after_time = get_time()
print("Script evaluated ", time_difference(before_time, after_time), "seconds")
print("Script succeed after", k, "times")
