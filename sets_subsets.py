'''
Given two sets, Checks if One Set is Subset or superset of Another Set. if the subset is found delete all elements from that set.
'''
ls1 = {27, 43, 34}
ls2 = {34, 93, 22, 27, 43, 53, 48}

print("Is ls1 subset of ls2?: ", ls1.issubset(ls2))
print("Is ls2 subset of ls1?: ", ls2.issubset(ls1))

print("Is ls1 superset of ls2?: ", ls1.issuperset(ls2))
print("Is ls2 superset of ls1?: ", ls2.issuperset(ls1))

if ls1.issubset(ls2):
    ls1.clear()
print(ls1)
