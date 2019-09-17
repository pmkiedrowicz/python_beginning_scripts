'''
Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element
'''

ls = [11, 45, 8, 11, 23, 45, 23, 45, 89, 2]
# Clear dictionary
hashmap = {}
# Counter
i = 0
# While theres next element of ls
while i < len(ls):
    num = ls[i]
    # Get the value of dictionary
    hash_value = hashmap.get(num)
    # If key is not preset, assign value 0
    if hash_value is None:
        hash_value = 0
    # Increment value
    hash_value += 1
    # Create new/update key/value
    temp = {ls[i]: hash_value}
    # Update dictionary
    hashmap.update(temp)
    # Increment counter
    i += 1

print(str(hashmap))
