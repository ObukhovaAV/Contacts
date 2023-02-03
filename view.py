


actions = [ " Показать все контакты",
            " Найти контакт",
            " Добавить контакт",
            " Редактировать контакт",
            " Удалить контакт",
            " Выход"]

def menu():
    print('Главное меню')
    for i, item in enumerate(actions, 1):
        print(f'{i}.{item}')
    choice = int(input('Выберите пункт меню '))
    return choice

def show_contacts(phone_list:list):    
    if len(phone_list) < 1:
        print('Список контактов пуст ')
    else:
        print()
        for i, c in enumerate(phone_list, 1):
            print(f'{i}.{c[0]:20} {c[1]:20}')
        print()

def input_error():
    print("Ошибка ввода ")
    
def create_contact():
    name = input('Введите имя и фамилию ')
    phone = input('Введите номер телефона ')
    return name, phone

def find_contact():
    find = input('Введите искомый элемент ')
    return find

def find_contact_del():
    find = input('Введите имя и фамилию ')
    return find

def show_contacts_new(phone_list:list):    
    if len(phone_list) < 1:
        print('Список контактов пуст ')
    else:        
        for i, c in enumerate(phone_list, 1):
            print(f'{i}.{c}')
              

