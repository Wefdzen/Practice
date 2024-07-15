#удаление либо по названию книги или по айди
import csv
import os

with open('DataBaseOfBook.csv', 'r', encoding='utf8') as inp, open('DataBaseOfBooked.csv', 'w', encoding='utf8', newline='') as out:
    writer = csv.writer(out)
    ans = True
    value_for_delete_by_id = ""
    value_for_delete_by_name = ""
    while ans:
        value_for_delete = str(input("Enter by what delete id or name(id/name): "))
        if value_for_delete == "id":
            value_for_delete_by_id = str(input("Enter id of book: "))
            ans = False
        elif value_for_delete == "name":
            value_for_delete_by_name = input("Enter name of book: ")
            ans = False
        else: 
            print("INCORRECT INPUT try again")

    def chose_index_csv():            #get index in csv file id or name book
        if value_for_delete_by_id != "":
            return 0
        elif value_for_delete_by_name != "":
            return 1
        else:
            return -1
    #delete the row
    end_choice = chose_index_csv()  # index for delete
    
    if value_for_delete_by_id != "":
        for row in csv.reader(inp):                 
            if row[end_choice] != value_for_delete_by_id:
                writer.writerow(row)
    elif value_for_delete_by_name != "":
        for row in csv.reader(inp):                 
            if row[end_choice] != value_for_delete_by_name:
                writer.writerow(row)
inp.close()
out.close()
os.remove("DataBaseOfBook.csv")
os.rename("DataBaseOfBooked.csv", "DataBaseOfBook.csv")

