'''
Generate a random Password which meets the following conditions:
Password length must be 10 characters long.
It must contain at least 2 upper case letter, 2 digits, and 2 special symbols.
'''
import string
from random import *


# Check length
def long_enough(pw):
    return len(pw) == 10


# Check uppercase
def uppercase(pw):
    return len(set(string.ascii_uppercase).intersection(pw)) > 1


# Check special characters
def special(pw):
    return len(set(string.punctuation).intersection(pw)) > 1


# Check numbers
def nums(pw):
    return len(set(string.digits).intersection(pw)) > 1


# Run each test, return fail if any return False
def test_password(pw, tests=[long_enough, uppercase, special, nums]):
    for test in tests:
        if not test(pw):
            return False
    return True


# Group of characters to build a password
characters = string.ascii_letters + string.punctuation + string.digits


def main():
    # Additional counter
    i = 1
    # Main flag
    flag = False
    # While flag is False, generate new password, increment counter and test again
    while not flag:
        password = "".join(choice(characters) for x in range(randint(10, 10)))
        if test_password(password):
            flag = True
        i += 1
    print("After", i, "rounds final password is:", password)


if __name__ == "__main__":
    main()
