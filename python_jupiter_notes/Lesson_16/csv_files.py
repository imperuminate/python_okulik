import csv


with open("data.csv", newline="") as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

for name, lname, city in data:
    print(name, lname, city)


with open("data.csv", newline="") as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

for row in data:
    print(row)