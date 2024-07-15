import csv

data  = ["id", "name", "priceD", "priceWD", "numOfFollowers","old", "student"]

with open("DataBaseOfBook.csv", "a", encoding='utf8', newline='') as f: #open file
    writer = csv.writer(f)
    for i, item in enumerate(data):
        data[i] = input(f"Give the {item}: ")
    writer.writerow(data)        #or writerows
    data  = ["id", "name", "priceD", "priceWD", "numOfFoll","old", "student"]#update for next use
f.close()

