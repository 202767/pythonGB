from return_data_file import data_file


def copy_file():
    data_1, nf_1 = data_file()
    count_rows_1 = len(data_1)
    if count_rows_1 == 0:
        print("Файл пустой!")
    else:
        number_row_1 = int(input(f"Введите номер строки "
                                 f"от 1 до {count_rows_1}: "))
        while number_row_1 < 1 or number_row_1 > count_rows_1:
            number_row_1 = int(input(f"Ошибка!"
                                     f"Введите номер строки "
                                     f"от 1 до {count_rows_1}: "))
    nf_2 = int(input("Выберите файл, куда скопировать строку\n"
                     "Введите цифру 1 или 2: "))
    while nf_2 < 1 or nf_2 > 2:
        nf_2 = int(input("Ошибка!!!\n"
                         "Введите цифру 1 или 2: "))
    with open(f'db/data{nf_2}.txt', 'r', encoding='utf-8') as file:
        data_2 = file.readlines()
    now_number_row = len(data_2) + 1
    with open(f'db/data{nf_2}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row};'
                   f'{data_1[number_row_1-1].split(";")[1]};'
                   f'{data_1[number_row_1-1].split(";")[2]};'
                   f'{data_1[number_row_1-1].split(";")[3]};'
                   f'{data_1[number_row_1-1].split(";")[4]}\n')
        print("Строка успешно скопирована!")
