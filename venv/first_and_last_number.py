'''
If in a given list first and last num equals, print information that they equals.
'''


# Check if given list length is more than one
def list_length(list):
    return len(list) > 1


# Given lists
lists = [(6, 55, 23, 8, 22, 6), (7, 7), (1, 2, 3, 4, 5, 6), (),(66,77,55,22)]
# Single list to assign each iteration - code readible
list = []
# Counter to increment in loop
counter = 0
# While counter is less than number of lists
while counter < len(lists):
    # Assign current list to list[]
    list = lists[counter]
    # Check for length of list, if false print "Invalid" information
    if list_length(list):
        print(
            "List is valid. First element: " + str(list[0]) + ", last element: " + str(
                list[len(list) - 1]) + "  ======  Given list: " + str(list))
    else:
        print("List is invalid. " + str(list))
    counter += 1
# if list_length(list):
#     list_len = len(list)
# else:
#     print("Wrong.")
