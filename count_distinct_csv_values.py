'''
Count total cars per company.
'''

import pandas

# Read .csv file
pd = pandas.read_csv("Automobile_data.csv")
# Transform into DataFrame
df = pandas.DataFrame(pd)

df = df['company'].value_counts()

print(df)
