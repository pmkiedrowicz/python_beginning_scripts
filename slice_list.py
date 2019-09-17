'''
Given a list slice it into a 3 equal chunks and revert each list
'''


def reverse_list(lis):
    return lis.reverse()


# Basic list
ls = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# How many parts of list is needed
part = len(ls) / 3
# Begin of slicing position
begin = 0
while begin < len(ls):
    # End of slicing position
    end = begin + int(part)
    # Slice list into small piece, assign to chunk_list object
    chunk_list = ls[begin:end]
    # Reverse the chunk_list and print it
    reverse_list(chunk_list)
    print(chunk_list)
    # Increment begin position by part value
    begin += int(part)
