'''
Basic script of multiplying two numbers. Also check if any of nums is not valid.
'''


# return true if number is a digit
def is_number(num):
    return num.isdigit()


# multiply two numbers
def multiple_numbers(num1, num2):
    return num1 * num2


print("Write values, accept with Enter, write any letter to continue program")

num1 = input("Write num1 ")
num2 = input("Write num2 ")

if is_number(num1) and is_number(num2):
    print(multiple_numbers(int(num1), int(num2)))
else:
    print("Atleast one num is not valid. Program will finish.")
