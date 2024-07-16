from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import csv
import os
import matplotlib.pyplot as plt
import pandas as pd

root = Tk() #window

def append_to_file():
    window1 = Toplevel(root) # Создаем новое окно
    window1.title("APPEND")
    window1.geometry("450x350")

    data = ["id", "name", "priceD", "priceWD", "numOfFollowers", "old", "student"]
    temp_data = [""] * len(data)# Хранение временных данных для всех полей


    def get_message(index):
        temp_data[index] = entry.get()  # Сохранение введенных данных
        temp_label["text"] = temp_data[index]# Обновление метки
        entry.delete(0, END) # Очистка поля ввода

        if index < len(data) - 1:
            entry_label["text"] = f"Enter {data[index + 1]}:"# Обновление метки для следующего ввода
            btn.config(command=lambda: get_message(index + 1)) # Обновление команды кнопки
        else:
            # Запись данных в файл после ввода всех полей
            with open("DataBaseOfBook.csv", "a", encoding='utf8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(temp_data)
            temp_label["text"] = "Data saved!"
            window1.after(2000, window1.destroy) # Закрытие окна

    entry_label = ttk.Label(window1, text=f"Enter {data[0]}:")
    entry_label.place(x=10, y=10, width=150, height=30)

    entry = ttk.Entry(window1)  
    entry.place(x=10, y=40, width=200, height=30)

    btn = ttk.Button(window1, text="Next", command=lambda: get_message(0))  # Кнопка для ввода первого поля
    btn.place(x=10, y=80, width=100, height=30)  

    temp_label = ttk.Label(window1)
    temp_label.place(x=10, y=120, width=200, height=30)

def delete_from_file():
    window1 = Toplevel(root)
    window1.title("DELETE")
    window1.geometry("450x250")

    def perform_deletion(value_for_delete, value):
        with open('DataBaseOfBook.csv', 'r', encoding='utf8') as inp, open('DataBaseOfBooked.csv', 'w', encoding='utf8', newline='') as out:
            writer = csv.writer(out)
            end_choice = 0 if value_for_delete == "id" else 1
            
            for row in csv.reader(inp):
                if row[end_choice] != value:
                    writer.writerow(row)
        
        os.remove("DataBaseOfBook.csv")
        os.rename("DataBaseOfBooked.csv", "DataBaseOfBook.csv")
        temp_label["text"] = "Data deleted!"
        window1.after(2000, window1.destroy) # Закрытие окна через 2 секунды

    def get_value_for_delete():
        value_for_delete = delete_option.get()
        value = entry.get()
        perform_deletion(value_for_delete, value)
    
    ttk.Label(window1, text="Enter by what to delete (id/name):").place(x=10, y=10)
    delete_option = StringVar(value="id")
    ttk.Radiobutton(window1, text="ID", variable=delete_option, value="id").place(x=10, y=30)
    ttk.Radiobutton(window1, text="Name", variable=delete_option, value="name").place(x=60, y=30)
    
    ttk.Label(window1, text="Enter value:").place(x=10, y=60)
    entry = ttk.Entry(window1)
    entry.place(x=10, y=90, width=200, height=30)

    btn = ttk.Button(window1, text="Delete", command=get_value_for_delete)
    btn.place(x=10, y=130, width=100, height=30)

    temp_label = ttk.Label(window1)
    temp_label.place(x=10, y=170, width=200, height=30)
  
def search_in_file():
    def perform_search(choice_index_of_user, user_choice, comparison=None):
        result_text.delete(1.0, END)
        try:
            with open("DataBaseOfBook.csv", "r", encoding='utf8') as f:
                reader = csv.reader(f)
                next(reader)  # Пропускаем заголовок
                for line in reader:
                    if len(line) < 7:  # Проверяем, что строка содержит достаточное количество элементов
                        continue
                    match choice_index_of_user:
                        case 0:
                            if line[choice_index_of_user] == user_choice:
                                result_text.insert(END, f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                                                     f'\nPRICE without deliver: {line[3]} , COUNT followers: {line[4]} , '
                                                     f'DISCOUNT for old people: {line[5]} , DISCOUNT for student: {line[6]}\n\n')
                        case 1:
                            if line[choice_index_of_user] == user_choice:
                                result_text.insert(END, f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                                                     f'\nPRICE without deliver: {line[3]} , COUNT followers: {line[4]} , '
                                                     f'DISCOUNT for old people: {line[5]} , DISCOUNT for student: {line[6]}\n\n')
                        case 2:
                            if (comparison == 1 and int(line[choice_index_of_user]) == int(user_choice)) or \
                               (comparison == 2 and int(line[choice_index_of_user]) >= int(user_choice)) or \
                               (comparison == 3 and int(line[choice_index_of_user]) <= int(user_choice)):
                                result_text.insert(END, f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                                                     f'\nPRICE without deliver: {line[3]} , COUNT followers: {line[4]} , '
                                                     f'DISCOUNT for old people: {line[5]} , DISCOUNT for student: {line[6]}\n\n')
                        case 3:
                            if (comparison == 1 and int(line[choice_index_of_user]) == int(user_choice)) or \
                               (comparison == 2 and int(line[choice_index_of_user]) >= int(user_choice)) or \
                               (comparison == 3 and int(line[choice_index_of_user]) <= int(user_choice)):
                                result_text.insert(END, f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                                                     f'\nPRICE without deliver: {line[3]} , COUNT followers: {line[4]} , '
                                                     f'DISCOUNT for old people: {line[5]} , DISCOUNT for student: {line[6]}\n\n')
                        case 4:
                            if (comparison == 1 and int(line[choice_index_of_user]) == int(user_choice)) or \
                               (comparison == 2 and int(line[choice_index_of_user]) >= int(user_choice)) or \
                               (comparison == 3 and int(line[choice_index_of_user]) <= int(user_choice)):
                                result_text.insert(END, f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                                                     f'\nPRICE without deliver: {line[3]} , COUNT followers: {line[4]} , '
                                                     f'DISCOUNT for old people: {line[5]} , DISCOUNT for student: {line[6]}\n\n')
                        case 5:
                            if line[choice_index_of_user] == user_choice:
                                result_text.insert(END, f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                                                     f'\nPRICE without deliver: {line[3]} , COUNT followers: {line[4]} , '
                                                     f'DISCOUNT for old people: {line[5]} , DISCOUNT for student: {line[6]}\n\n')
                        case 6:
                            if line[choice_index_of_user] == user_choice:
                                result_text.insert(END, f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                                                     f'\nPRICE without deliver: {line[3]} , COUNT followers: {line[4]} , '
                                                     f'DISCOUNT for old people: {line[5]} , DISCOUNT for student: {line[6]}\n\n')
                        case 999:
                            result_text.insert(END, f'ID: {line[0]} , NAME: {line[1]} , PRICE with deliver: {line[2]} ,' 
                                                 f'\nPRICE without deliver: {line[3]} , COUNT followers: {line[4]} , '
                                                 f'DISCOUNT for old people: {line[5]} , DISCOUNT for student: {line[6]}\n\n')
        except Exception as e:
            result_text.insert(END, f"Error: {str(e)}\n")

    def get_search_criteria():
        value_for_find = int(search_option.get())
        user_choice = entry.get()
        choice_index_of_user = 0
        comparison = None

        match value_for_find:
            case 1:
                choice_index_of_user = 0
            case 2:
                choice_index_of_user = 1
            case 3:
                choice_index_of_user = 2
                comparison = int(comparison_option.get())
            case 4:
                choice_index_of_user = 3
                comparison = int(comparison_option.get())
            case 5:
                choice_index_of_user = 4
                comparison = int(comparison_option.get())
            case 6:
                choice_index_of_user = 5
            case 7:
                choice_index_of_user = 6
            case 8:
                choice_index_of_user = 999
            case _:
                print("Invalid choice")

        perform_search(choice_index_of_user, user_choice, comparison)

    window1 = Toplevel(root)
    window1.title("Search")
    window1.geometry("800x400")

    ttk.Label(window1, text="Enter which setting you want to search (1.id/2.name/3.priceD/4.priceWD/5.numOfFoll/6.oldDiscount/7.studentDiscount/8.all_base):").place(x=10, y=10)
    search_option = StringVar(value="1")
    ttk.Combobox(window1, textvariable=search_option, values=[1, 2, 3, 4, 5, 6, 7, 8]).place(x=10, y=30)

    ttk.Label(window1, text="Enter value:").place(x=10, y=60)
    entry = ttk.Entry(window1)
    entry.place(x=10, y=80, width=200, height=30)

    ttk.Label(window1, text="Settings only for priceD/priceWD/numOfFoll (1.=  2.>=  3<=):").place(x=10, y=110)
    comparison_option = StringVar(value="1")
    ttk.Combobox(window1, textvariable=comparison_option, values=[1, 2, 3]).place(x=10, y=130)

    btn = ttk.Button(window1, text="Search", command=get_search_criteria)
    btn.place(x=10, y=170, width=100, height=30)

    result_text = Text(window1, wrap='word')
    result_text.place(x=10, y=210, width=580, height=180)

def update_record():
    window1 = Toplevel(root)
    window1.title("Update Record")
    window1.geometry("600x400")

    def perform_update(index_to_find, value_to_find, field_to_update, new_value):
        with open('DataBaseOfBook.csv', 'r', encoding='utf8') as inp, open('DataBaseOfBooked.csv', 'w', encoding='utf8', newline='') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if len(row) > max(index_to_find, field_to_update) and row[index_to_find] == value_to_find:
                    row[field_to_update] = new_value
                writer.writerow(row)
        
        os.remove("DataBaseOfBook.csv")
        os.rename("DataBaseOfBooked.csv", "DataBaseOfBook.csv")
        result_label.config(text="Record updated successfully!")

    def get_update_criteria():
        field_to_find = search_option.get()
        value_to_find = entry_find.get()
        field_to_update = update_option.get()
        new_value = entry_new_value.get()
        
        field_map = {
            "id": 0,
            "name": 1,
            "priceD": 2,
            "priceWD": 3,
            "numOfFollowers": 4,
            "oldDiscount": 5,
            "studentDiscount": 6
        }

        index_to_find = field_map.get(field_to_find, None)
        index_to_update = field_map.get(field_to_update, None)

        if index_to_find is not None and index_to_update is not None:
            perform_update(index_to_find, value_to_find, index_to_update, new_value)
        else:
            result_label.config(text="Invalid field selected for search or update")

    ttk.Label(window1, text="Enter field to find (id/name/priceD/priceWD/numOfFollowers/oldDiscount/studentDiscount):").place(x=10, y=10)
    search_option = StringVar(value="id")
    ttk.Combobox(window1, textvariable=search_option, values=["id", "name", "priceD", "priceWD", "numOfFollowers", "oldDiscount", "studentDiscount"]).place(x=10, y=30)

    ttk.Label(window1, text="Enter value to find:").place(x=10, y=60)
    entry_find = ttk.Entry(window1)
    entry_find.place(x=10, y=80, width=200, height=30)

    ttk.Label(window1, text="Enter field to update (id/name/priceD/priceWD/numOfFollowers/oldDiscount/studentDiscount):").place(x=10, y=110)
    update_option = StringVar(value="id")
    ttk.Combobox(window1, textvariable=update_option, values=["id", "name", "priceD", "priceWD", "numOfFollowers", "oldDiscount", "studentDiscount"]).place(x=10, y=130)

    ttk.Label(window1, text="Enter new value:").place(x=10, y=160)
    entry_new_value = ttk.Entry(window1)
    entry_new_value.place(x=10, y=180, width=200, height=30)

    btn = ttk.Button(window1, text="Update", command=get_update_criteria)
    btn.place(x=10, y=220, width=100, height=30)

    result_label = ttk.Label(window1, text="")
    result_label.place(x=10, y=260)

# Новая функция для отображения графиков
def show_statistics():
    try:
        data = pd.read_csv("DataBaseOfBook.csv")
        data2 = pd.read_csv("DataBaseOfHuman.csv")
        window1 = Toplevel(root)
        window1.title("Statistics")
        window1.geometry("800x600")
        
        #функция для подсчета сколько клиентов студентов old или other
        def plot_popular_editions():
            if 'OldStudentNot' not in data2.columns:
                print("Column 'OldStudentNot' is not present in the data.")
                return
            
            plt.figure(figsize=(10, 6))
            
            # Подсчет количества для каждого типа
            old_student_not_counts = data2['OldStudentNot'].value_counts()
            
            # Построение гистограммы
            old_student_not_counts.plot(kind='bar', color='skyblue')
            
            plt.title('Распределение поколений')
            plt.xlabel('Категория')
            plt.ylabel('Счет')
            
            # Установка меток оси X
            ticks = range(len(old_student_not_counts))
            labels = ['Old поколение', 'Студенты', 'Остальные']
            plt.xticks(ticks, labels, rotation=0)
            
            plt.tight_layout()
            plt.show()
        #функция для подсчета сколько клиентов используют доставку
        def plot_services_distribution():
            if 'Delivery_or_not' not in data2.columns:
                print("Column 'Delivery_or_not' is not present in the data.")
                return
            
            plt.figure(figsize=(10, 6))
            
            # Подсчет количества подписок с доставкой и без доставки
            delivery_counts = data2['Delivery_or_not'].value_counts()
            
            # Построение круговой диаграммы
            delivery_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen'])
            
            plt.title('Распределение услуг по доставке')
            plt.ylabel('')
            plt.show()
        #функция для вывода книг и кол-во их подписчиков
        def plot_followers_histogram():
            if 'name' not in data.columns or 'numOfFollowers' not in data.columns:
                print("Columns 'name' or 'numOfFollowers' are not present in the data.")
                return
            
            plt.figure(figsize=(10, 6))
            
            # Группировка данных по названию книги и суммирование количества подписчиков для каждой книги
            followers_per_book = data.groupby('name')['numOfFollowers'].sum()
            
            # Построение столбчатой диаграммы
            followers_per_book.plot(kind='bar', color='lightgreen', edgecolor='black')
            
            plt.title('Количество подписчиков на книгу')
            plt.xlabel('Название книг')
            plt.ylabel('Кол-во подписчиков')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        #output button to window1
        btn_popular_editions = ttk.Button(window1, text="Распределение поколений", command=plot_popular_editions)
        btn_popular_editions.place(x=10, y=10, width=200, height=30)

        btn_services_distribution = ttk.Button(window1, text="Распределение услуг по доставке", command=plot_services_distribution)
        btn_services_distribution.place(x=10, y=50, width=200, height=30)

        btn_followers_histogram = ttk.Button(window1, text="Кол-во подписчиков на книгу", command=plot_followers_histogram)
        btn_followers_histogram.place(x=10, y=90, width=200, height=30)
    
    except FileNotFoundError:
        print("CSV file not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("CSV file is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    except FileNotFoundError:
        print("CSV file not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("CSV file is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Config of application
root.title("Менеджер Подписок")
root.iconbitmap(default="source_images\emblema_of_app.ico")
root.geometry("1080x720+400+200")
root.resizable(False, False)

# MAIN LABEL
main_label = ttk.Label(text="Удобный менеджер с бд", font=("Arial", 20))
main_label.pack()

# Start input image
image = Image.open("source_images/pngwing.com.png")
image_width, image_height = image.size
just_photo = ImageTk.PhotoImage(image)
canvas = Canvas(root, bg="white", width=700, height=700)
x_center = (700 - image_width) // 2
y_center = (700 - image_height) // 2
canvas.create_image(x_center, y_center, anchor=NW, image=just_photo)
canvas.pack()

# BUTTONS
btn_add_DataBase = ttk.Button(text="Добавить запись в бд", command=append_to_file)
btn_add_DataBase.place(x=10, y=100, width=200, height=125)

btn_del_DataBase = ttk.Button(text="Удалить запись из бд", command=delete_from_file)
btn_del_DataBase.place(x=350, y=100, width=200, height=125)    

btn_search_DataBase = ttk.Button(text="Поиск записи в бд", command=search_in_file)
btn_search_DataBase.place(x=10, y=310, width=200, height=125)

btn_change_DataBase = ttk.Button(text="Изменить запись в бд", command=update_record)
btn_change_DataBase.place(x=350, y=310, width=200, height=125)  

btn_statistics = ttk.Button(text="Статистики", command=show_statistics)
btn_statistics.place(x=700, y=100, width=200, height=125)

root.mainloop()
