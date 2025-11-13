import csv

filename = "mobile_products.csv"
headers= []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader)

    for row in csvreader:
        rows.append(row)

print("Header names are :")
for header in headers:
    print(header)

print("Row contents")
for i in range(10):
    

