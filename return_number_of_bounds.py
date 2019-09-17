'''
Return a number of given string bounds
'''

str = "Emma is a good developer. Emma is also a writer, and output should be 2."
sub = "Emma"

print("Given String: " + str)
print("Given substring: " + sub)
print("Word " + sub + " appeared", str.count(sub), "times.")
