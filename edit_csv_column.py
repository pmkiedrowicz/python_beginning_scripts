'''
Find the most expensive car company name
Print most expensive car’s company name and price.
'''
import pandas

# Read .csv file
pd = pandas.read_csv("Automobile_data.csv")
# Transform into DataFrame
df = pandas.DataFrame(pd)
# Sort column values by 'price', with descending mode, select one row
df = df.sort_values('price', ascending=False).head(1)
# Prepare output to choosen columns index,company,price
df = df[['index', 'company', 'price']]
print(df)
