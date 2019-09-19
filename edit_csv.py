'''
Clean data and update the CSV file
Replace all column values which contain ‘?’ and n.a with NaN.
'''
import pandas

obj = pandas.read_csv("Automobile_data.csv", na_values={
    'index': ["?", "n.a"],
    'company': ["?", "n.a"],
    'body-style': ["?", "n.a"],
    'wheel-base': ["?", "n.a"],
    'length': ["?", "n.a"],
    'engine-type': ["?", "n.a"],
    'num-of-cylinders': ["?", "n.a"],
    'horsepower': ["?", "n.a"],
    'average-mileage': ["?", "n.a"],
    'price': ["?", "n.a"],
})
# obj.replace("?n.a", "NaN")
print(obj)
