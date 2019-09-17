'''
Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.
'''

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]


# Pick even numbers from list
def pick_even_index(ls):
    return ls[::2]


# Pick odd numbers from list
def pick_odd_index(ls):
    i = 1
    new_ls = []
    while i < len(ls):
        if ls[i] % 2 == 0:
            new_ls.append(ls[i])
        i += 2
    return new_ls


# Create final list with both lists
final_list = pick_odd_index(listOne) + pick_even_index(listTwo)
print(final_list)
