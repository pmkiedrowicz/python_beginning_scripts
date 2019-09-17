'''
Given a following two sets find the intersection and remove those elements from the first set
'''

# Basic two sets
ls1 = {65, 42, 78, 83, 23, 57, 29}
ls2 = {67, 73, 43, 48, 83, 57, 29}

# Get the duplicated values of sets, and assign them to new set
duplicated = ls1.intersection(ls2)

# Iterate through duplicated values, and remove them from ls1 list
for obj in duplicated:
    ls1.remove(obj)
print(ls1)
