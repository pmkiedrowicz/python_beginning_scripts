'''
Script prints only even characters.
'''
# input user string
str = input("Please write a string: ")
# counter to print even characters
i = 0
# while length of string is less than counter
# print even characters and add 2 to counter
while len(str) > i:
    print(str[i])
    i += 2
