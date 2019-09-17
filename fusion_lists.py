'''
Given a two list of equal size create a set such that it shows the element from both lists in the pair.
'''

ls1 = [2, 3, 4, 5, 6, 7, 8]
ls2 = [4, 9, 16, 25, 36, 49, 64]

# zip two lists into object
result_list = zip(ls1, ls2)
# set pairs
result = set(result_list)
print(result)
