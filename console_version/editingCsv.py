import csv
import os
#TODO сделать мб более 1 выбора типо нетоко выбор 1 усл а несколько
with open('DataBaseOfBook.csv', 'r', encoding='utf8') as inp, open('DataBaseOfBooked.csv', 'w', encoding='utf8', newline='') as out:
    writer = csv.writer(out)
    ans = True
    value_for_find_by_id = ""
    value_for_find_by_name = ""
    updateValue_for_find_end = 0
    #ENTER OF BOOK
    while ans:
        value_for_find = str(input("enter which book you want to change its name or ID :waiting(id/name): "))
        if value_for_find == "id":
            value_for_find_by_id = str(input("Enter id of book: "))
            ans = False
        elif value_for_find == "name":
            value_for_find_by_name = str(input("Enter name of book: "))
            ans = False
        else: 
            print("INCORRECT INPUT try again")
   
    if value_for_find == "id":
        updateValue_for_find_end = 0
    elif value_for_find == "name":
        updateValue_for_find_end = 1
    else:
        print("Error")
            
    #ENTER of field
    def chose_index_csv():            #get index in csv file 
        value_for_change = int(input("Enter what edit of the book (1.id/2.name/3.priceD/4.priceWD/5.numOfFoll/6.oldDiscount/7.studentDiscount): "))
        match value_for_change: 
            case 1:
                return 0
            case 2:
                return 1
            case 3:
                return 2
            case 4:
               return 3
            case 5:
                return 4
            case 6:
                return 5
            case 7:
                return 6 
            case _:
                print("INCORRECT INPUT try again")
                return -1
    end_choice = chose_index_csv()  # index for edit
    #Change of field #TODO доделать комм что это внизу
    if value_for_find == "id":
        updateValue_for_find_end = 0
    elif value_for_find == "name":
        updateValue_for_find_end = 1
    else:
        print("Error")
    if updateValue_for_find_end == 0: 
        value_for_compare = value_for_find_by_id
    elif updateValue_for_find_end == 1:
        value_for_compare = value_for_find_by_name

    match end_choice:
        case 0: #change id
            print("0")
            for row in csv.reader(inp):
                if row[updateValue_for_find_end] == value_for_compare:
                    book_new_id = str(input("Enter new id of book: "))
                    row[end_choice] = book_new_id
                    writer.writerow(row)
                else: #остальное то перезаписать придется
                    writer.writerow(row)
        case 1: #change name
             print("1")  
             for row in csv.reader(inp):
                if row[updateValue_for_find_end] == value_for_compare:
                    book_new_name = str(input("Enter new name of book: "))
                    row[end_choice] = book_new_name
                    writer.writerow(row)
                else: #остальное то перезаписать придется
                    writer.writerow(row) 
        case 2: #change priceD
            print("2")
            for row in csv.reader(inp):
                if row[updateValue_for_find_end] == value_for_compare:
                    book_new_priceD = str(input("Enter new price for book with deliver: "))
                    row[end_choice] = book_new_priceD
                    writer.writerow(row)
                else: #остальное то перезаписать придется
                    writer.writerow(row) 
        case 3: #change priceWD
            print("3")
            for row in csv.reader(inp):
                if row[updateValue_for_find_end] == value_for_compare:
                    book_new_priceWD = str(input("Enter new price for book without deliver: "))
                    row[end_choice] = book_new_priceWD
                    writer.writerow(row)
                else: #остальное то перезаписать придется
                    writer.writerow(row)
        case 4: # change followers
            print("4")
            for row in csv.reader(inp):
                if row[updateValue_for_find_end] == value_for_compare:
                    book_new_numOfFoll = str(input("Enter new price for book without deliver: "))        
                    row[end_choice] = book_new_numOfFoll
                    writer.writerow(row)
                else: #остальное то перезаписать придется
                    writer.writerow(row)
        case 5: #change old
            print("5")
            for row in csv.reader(inp):
                if row[updateValue_for_find_end] == value_for_compare:
                    book_new_old = str(input("Enter new old people discount for book : "))
                    row[end_choice] = book_new_old
                    writer.writerow(row)
                else: #остальное то перезаписать придется
                    writer.writerow(row)
        case 6:
            print("6")
            for row in csv.reader(inp):
                if row[updateValue_for_find_end] == value_for_compare:
                    book_new_student = str(input("Enter new student people discount for book : "))        
                    row[end_choice] = book_new_student
                    writer.writerow(row)
                else: #остальное то перезаписать придется
                    writer.writerow(row)

        case _:
            print("Inocorrect end_choice!!!")

inp.close()
out.close()
os.remove("DataBaseOfBook.csv")
os.rename("DataBaseOfBooked.csv", "DataBaseOfBook.csv")