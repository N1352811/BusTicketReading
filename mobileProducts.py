import csv

filename = "mobile_products.csv"
headers= []
datalist = []

with open(filename, mode= 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        datalist.append(row)


print(datalist[0])

for row in datalist:
    print(row["topup_title"],row["topup_price_in_pence"])
    

