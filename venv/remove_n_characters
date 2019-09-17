'''
Type a string, then remove characters from index 0 to a typed index.
Return new string.
'''


# return true if number is a digit
def is_number(num):
    return num.isdigit()


str = input("Type a string to slice it up: ")
num = input("Input to which character slice it up: ")
# First check if given num is a positive number
if is_number(num):
    # Assign num value to integer
    num = int(num)
    # If num equals zero, finish program.
    if num == 0:
        print("Num equals 0. This way is not gonna return anything.")
    # If length of given string is less than 1, finish program.
    elif int(len(str)) < 1:
        print("Given string looks empty. Program will exit.")
    # If length of string is more or equals num, return slice string.
    elif int(len(str)) >= num:
        print(str[0:num])
    else:
        print("Given num is too big. Program will exit.")
else:
    print("Num is not a valid number. Program will exit.")
