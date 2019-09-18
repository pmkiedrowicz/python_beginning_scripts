'''
Calculate mutiplication of two random float number.
First random float number must be between 0.1 and 1
Second random float number must be between 9.5 and 99.5
'''
import random


def small_float():
    return random.random()


def big_float():
    return random.uniform(9.5, 99.5)


small = small_float()
big = big_float()

print("Random float between 0.1 and 1: ", small)
print("Random float between 9.5 and 99.5: ", big)
print("Multiplication value of these floats: ", small * big)
