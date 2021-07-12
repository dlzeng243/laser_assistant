import csv

f = open("./test_excel.csv")
csv_reader = csv.DictReader(f)
for line in csv_reader:
    print(line)
    if line["hi"] == None:
        print("hi")