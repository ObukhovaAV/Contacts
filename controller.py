from view import*
from model import*

def start():
    choice = ''
    while choice != 7:
        choice = menu()
    
        match choice:
            case 1:
                open_file()
                show_contacts(get_contacts())
            case 2:
                find = find_contact()
                result = search_contact(find)
                show_contacts_new(result)
            case 3:
                add_contact(create_contact())
            case 4:
                pass
            case 5:
                c_del = find_contact_del()
                total = del_contact(c_del)  
                show_contacts_new(total)
            case 6:
                print("Всего доброго!")
                break
            case _:
                input_error()