'''
Print a pattern:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''


# return true if number is a digit
def is_number(num):
    return num.isdigit()


# Get the number of bounds from a user
bounds = input("Type a num of bounds: ")
# First check if its actually a number
if is_number(bounds):
    # If number equals zero, print message
    if int(bounds) == 0:
        print("Num of bounds can't be zero.")
    # Else continue program
    else:
        # i counter for actual line
        i = 1
        # t counter for counter
        t = 1
        # strr to build line string
        strr = ""
        # while number line is less than number of bounds
        while i < int(bounds) + 1:
            # also while t counter is less or equals line number
            while t <= i:
                # concatenate string
                strr = strr + str(i) + " "
                t += 1
            print(strr)
            strr = ""
            i += 1
            t = 1
else:
    print("This is not a valid, positive number.")
