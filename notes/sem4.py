# Задача 25. Напишите программу, которая принимает на вход строку, и отследивает, сколько раз каждый символ уже встречался.
# Количество повтров добавляется к символам с помощью постфикса формата _n.
# str_1 = input("Введите строку: ")
# str_1 = str_1.split()
# my_dict = {}
# for i in str_1:
#     if i not in my_dict:
#         my_dict[i] = 1
#         print(i, end=" ")
#     else:
#         print(f"{i}_{my_dict[i]}", end=" ")
#         my_dict[i] += 1
# Задача 27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним пробелом.
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# str_1 = set(("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".upper()).split())
# print(len(str_1))
