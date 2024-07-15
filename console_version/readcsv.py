import csv

with open("DataBaseOfBook.csv", "r", encoding='utf8') as f: #open file
    reader = csv.reader(f)

    for line in reader:
        print(line[1])
f.close()