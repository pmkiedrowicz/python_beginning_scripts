'''
Merge two lists and find even numbers of it.
'''

# Basic two list
listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]

# Merge lists into new one
merged_list = listOne + listTwo
# Counter
i = 0

# While counter is less than length of merged list
while i < len(merged_list):
    # If given object of list modulo not equals 0, remove than object and set counter -1
    if merged_list[i] % 2 != 0:
        merged_list.remove(merged_list[i])
        i -= 1
    i += 1
print(merged_list)
