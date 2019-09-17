'''
Remove duplicate from a list and create a tuple and find the minimum and maximum number.
'''

ls = [87, 45, 41, 65, 94, 41, 99, 94]

uniq = set(ls)
print("Unique items: ", uniq)

tup = tuple(uniq)
print("Tuple items: ", tup)

print("Minimum value: ", min(tup))
print("Maximum value: ", max(tup))
