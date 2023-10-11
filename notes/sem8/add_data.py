from return_data_file import data_file


def add_row():

    name = input("Введите свое имя: ")
    surname = input("Введите свою фамилию: ")
    birthday = input("Введите дату рождения: ")
    city = input("Введите город проживания: ")
    data, nf = data_file()
    now_number_row = len(data) + 1
    with open(f'db/data{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        now_number_row = len(data) + 1
    with open(f'db/data{nf}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row};{name};'
                   f'{surname};{birthday};{city}\n')
    print("Данные успешно записаны!")
