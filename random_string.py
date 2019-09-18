'''
Generate  random String of length 5.
String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
'''

import random
import string


def generate_string(length):
    base_chars = string.ascii_letters
    return ''.join(random.choice(base_chars) for i in range(length))


print("Random string: ", generate_string(5))
