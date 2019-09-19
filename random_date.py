'''
Generate a random date between given start and end dates.
'''

import time
import random


def get_random_date(start, end):
    rg = random.random()
    format = '%m/%d/%Y'
    start_time = time.mktime(time.strptime(start, format))
    end_time = time.mktime(time.strptime(end, format))
    random_time = start_time + rg * (end_time - start_time)
    random_date = time.strftime(format, time.localtime(random_time))
    return random_date


print("Random date between 1/1/2000 and 1/1/2011: ", get_random_date("01/01/2000", "01/01/2011"))
