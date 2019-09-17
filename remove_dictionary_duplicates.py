'''
Given a dictionary get all values from the dictionary and add it in a list but don’t add duplicates.
'''

ls = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

ls2 = []
for i in ls.values():
    if i not in ls2:
        ls2.append(i)
print(ls2)
