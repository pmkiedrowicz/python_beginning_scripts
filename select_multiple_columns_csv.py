'''
Find each company’s Higesht price car
'''

import pandas

# Read .csv file
pd = pandas.read_csv("Automobile_data.csv")
# Create multidimension list grouped by company
companies = pd.groupby('company')
# Use below script for debugging
# for i in companies:
#     print(i)

# Select from each group row with max price value
max_price = companies['company', 'price'].max()

print(max_price)
