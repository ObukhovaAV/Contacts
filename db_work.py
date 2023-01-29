from os import path

from err_check import matching_rec, find_entry


all_data = {}
name_db = "contacts.txt"


def read_all():
    global all_data
    
    print(name_db)
    if path.exists(name_db):
        with open(name_db, "r", encoding="utf-8") as file:
            txt_reader = file.readlines()
            all_data = [i for i in txt_reader]
            return all_data
    else:
        print("The database is not connected!")


def print_all():
    global all_data
    for_output = [" ".join (k for k in all_data)]
    print(*for_output, sep="\n", end='')


def add_entry(data):
    if all(data) and matching_rec(data, all_data):
        
        with open(name_db, "a", encoding="utf-8") as file:
            file.writelines(str(data))
            print("Запись добавлена")
    else:
            print("Запись уже есть ")


def del_entry(data_del):
    global all_data

    id_cand = find_entry(data_del, all_data)
    if id_cand:
        id_del = input(f"Введите фамилию ")
       

        if id_del in id_cand:
            all_data = [k for k in all_data if k != id_del]
            with open(name_db, "w", encoding="utf-8", newline="") as file:
                
                file.write(all_data)
                
                print("Data deleted\n")
        else:
            
            print("Id not found.\n")
    

def edit_entry(data_change, id_change):
    global all_data
    key, value = data_change

    
    if find_entry(id_change, all_data):
        for i, v in enumerate(all_data):
            if v["id"] == id_change:
                
                v[key] = value
                
                all_data[i] = v

        with open(name_db, "w", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "name", "surname", "phone"]
            file.write(fieldnames)
            print("Data changed\n")
    else:
        
        print("Id not found.\n")



