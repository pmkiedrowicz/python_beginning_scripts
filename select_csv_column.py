'''
Print All Toyota Cars details.
'''

import pandas

# Read .csv file
pd = pandas.read_csv("Automobile_data.csv")
# Transform into DataFrame
df = pandas.DataFrame(pd)
# Filter output to only 'toyota' in column 'company'
df = df.loc[df['company'].isin(["toyota"])]

print(df)
