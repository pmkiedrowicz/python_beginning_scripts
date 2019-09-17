'''
Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list
'''
# Given list
ls = [34, 54, 67, 89, 11, 43, 94]
print(ls)
# Remove 4th index of list, also save into variable
num = ls.pop(4)
print(ls)
# Insert object into index 2 of list
ls.insert(2, num)
print(ls)
# Add object at the last place of list
ls.append(num)
print(ls)
