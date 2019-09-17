'''
Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list
'''

ls = [47, 64, 69, 37, 76, 83, 95, 97]
sample = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

ls[:] = [item for item in ls if item in sample.values()]
print(ls)