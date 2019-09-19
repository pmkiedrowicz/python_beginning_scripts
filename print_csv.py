'''
From given data set print first and last five rows.
'''

import pandas

obj = pandas.read_csv("Automobile_data.csv")
print(obj.head(5))

print(obj.tail(5))
