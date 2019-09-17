'''
Check if the reversed number equals the original one.
'''


# Print the final string
def print_string(string):
    return print(string)


# Parse int into string, then reverse it
def reverse_num(num):
    temp = str(num)
    return temp[::-1]


# Check, if both strings are equal
def check_equal_string(str1, str2):
    return str1 == str2


# Basic num_list
num_list = [12321,
            123321,
            0,
            121,
            12521,
            15511]

# Counter
i = 0

# While counter is less than length of num_list
while i < len(num_list):
    new_number = num_list[i]
    if new_number >= 0:
        new_number = reverse_num(new_number)
        if check_equal_string(str(num_list[i]), new_number):
            print_string(new_number)
    i += 1
