import csv

with open("DataBaseOfBook.csv", "r", encoding='utf8') as f: #open file
    reader = csv.reader(f)
    value_for_find = ""
    ans = True
    choice_index_of_user = 0
    #User choice and get index
    while ans:
        value_for_find = int(input("Enter which setting you want search \n(1.id/2.name/3.priceD/4.priceWD/5.numOfFoll/6.oldDiscount/7.studentDiscount/8.all_base): "))
        match value_for_find:
            case 1:
                choice_index_of_user = 0
                ans = False
            case 2:
                choice_index_of_user = 1
                ans = False
            case 3:
                choice_index_of_user = 2
                ans = False
            case 4:
                choice_index_of_user = 3
                ans = False
            case 5:
                choice_index_of_user = 4
                ans = False
            case 6:
                choice_index_of_user = 5
                ans = False
            case 7:
                choice_index_of_user = 6
                ans = False
            case 8:
                choice_index_of_user = 999
                ans = False
            case _:
                choice_index_of_user = -1
                print("NO!!!")

    
    #output
    match choice_index_of_user:
        case 0:
            itog_user_choice = str(input("enter id of book: "))
            for line in reader:
                if line[choice_index_of_user] == itog_user_choice: 
                    print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                    f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
        case 1:
            itog_user_choice = str(input("enter name of book: "))
            for line in reader:
                if line[choice_index_of_user] == itog_user_choice: 
                    print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                    f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
        case 2:
            itog_user_choice = int(input("enter price of book with deliver: "))
            user_priceD = int(input("enter symbol what find: 1.=   2.>=   3<=:  "))
            match user_priceD:
                case 1:
                    for line in reader:
                        if int(line[choice_index_of_user]) == itog_user_choice: 
                            print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                            f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
                case 2:
                    for line in reader:
                        if int(line[choice_index_of_user]) >= itog_user_choice: 
                            print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                            f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
                case 3:
                    for line in reader:
                        if int(line[choice_index_of_user]) <= itog_user_choice: 
                            print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                            f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
        case 3:
            itog_user_choice = int(input("enter price of book without deliver: "))
            user_priceWD = int(input("enter symbol what find: 1.=   2.>=   3<=:  "))
            match user_priceWD:
                case 1:
                    for line in reader:
                        if int(line[choice_index_of_user]) == itog_user_choice: 
                            print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                            f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
                case 2:
                    for line in reader:
                        if int(line[choice_index_of_user]) >= itog_user_choice: 
                            print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                            f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
                case 3:
                    for line in reader:
                        if int(line[choice_index_of_user]) <= itog_user_choice: 
                            print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                            f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
        case 4:
            itog_user_choice = int(input("enter count followers of book: "))
            user_follower = int(input("enter symbol what find: 1.=   2.>=   3<=:  "))
            match user_follower:
                case 1:
                    for line in reader:
                        if int(line[choice_index_of_user]) == itog_user_choice: 
                            print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                            f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
                case 2:
                    for line in reader:
                        if int(line[choice_index_of_user]) >= itog_user_choice: 
                            print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                            f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
                case 3:
                    for line in reader:
                        if int(line[choice_index_of_user]) <= itog_user_choice: 
                            print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                            f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
        case 5:
            itog_user_choice = str(input("enter have book old people discover or no book (y/n): "))
            for line in reader:
                if line[choice_index_of_user] == itog_user_choice:    # waitin in file y or n
                    print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                    f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
        case 6:
            itog_user_choice = str(input("enter have book student discover or no book (y/n):"))
            for line in reader:
                if line[choice_index_of_user] == itog_user_choice: 
                    print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                    f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
        case 999:
            for line in reader:
                print(f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                f'\nPRICE without deliver{line[3]} , COUNT followers: {line[4]} , DISCOUNT for old people: {line[5]} , DICSCOUNT for student: {line[6]}\n')
        case _:
            print("error")

    for line in reader:
        print(line[1])
f.close()