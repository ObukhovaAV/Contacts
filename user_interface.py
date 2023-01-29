from err_check import check_new_data
from db_work import *



def menu():
    while True:
        read_all()
        print(f"Контакты\n")
        actions = input("1. Показать все контакты\n"
                        "2. Найти контакт\n"
                        "3. Добавить контакт\n"
                        "4. Редактировать контакт\n"
                        "5. Удалить контакт\n"
                        "6. Выход\n")
        match actions:
            case "1":
                print_all()
            case "2":
                find_entry(input("Введите фамилию или номер телефона: "), read_all())
            case "3":
                add_entry(add_menu())
            case "4":
                print_all()
                id_change = input(f"Введите id: ")
                if find_entry(id_change, read_all()) and (answer := edit_menu()):
                    edit_entry(answer, id_change)
            case "5":
                del_entry(input("Введите фамилию или номер телефона: "))
            case "6":
                
                print("До новых встреч!")
                break
            case _:
               
                print("The data is not recognized, repeat the input.")


def add_menu():
    
    add_dict = {"имя": "", "фамилия": "", "номер телефона": ""}
    for i in add_dict:
        if i != "id":
            add_dict[i] = check_new_data(i)
    
    return add_dict


def edit_menu():
    add_dict = {"1": "name", "2": "surname", "3": "phone"}
    
    while True:
        print("\nChanging:")
        change = input("1. name\n"
                       "2. surname\n"
                       "3. phone\n"
                       "4. exit\n")

        match change:
            case "1" | "2" | "3":
                type_date = add_dict[change]
                return type_date, check_new_data(type_date)
            case "4":
                
                return 0
            case _:
               
                print("The data is not recognized, repeat the input.")


