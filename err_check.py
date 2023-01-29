


def find_entry(data_find, all_info):
    
    candidates = [" ".join(i for i in all_info if data_find in i)]
    if candidates:
        
        print(*candidates, sep="\n", end="\n\n")
        
    else:
        
        print("Name or phone number not found.\n")
        return 0


def matching_rec(new_entry: dict, all_info):
    value = list(new_entry)[1:]
    all_values = [list(k)[1:] for k in all_info]
    return value not in all_values


def check_new_data(num):
    answer = input(f"Введите {num}: ")
    while True:
        if num in "имя фамилия":
            if answer.isalpha():
                break
        if num == "номер телефона":
            if answer.isdigit() and len(answer) == 5:
                break
        answer = input(f"Данные некорректны\n"
                       f"Используйте только буквы "
                       f"длина номера телефона 5 цифр\n"
                       f"Введите {num}: ")
    return answer
