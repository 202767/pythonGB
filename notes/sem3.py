# Задача 17. Дан список чисел. Определите, сколько в нем встречается разных чисел
# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# list_1 = set(list_1)
# print(len(list_1))
# Задача 19. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность(сдвиг - циклический) на K элементов вправо, K - положительное число.
# list_1 = [1, 2, 3, 4, 5]
# k = int(input("Введите кол-во сдвигов: ")) % len(list_1)
# if k == 0:
#     print(list_1)
# else:
#     print(list_1[-k:]+list_1[:len(list_1)-k])
# Задача 21. Напишите программу для печати всех уникальных значний в словаре
# data = [{"V": "5001"}, {"V": "5002"}, {"VI": "5001"}, {
#     "VI": "5005"}, {"VII": "5005"}, {"V": "5009"}, {"VIII": "5007"}]
# set_values = set()
# for i in data:
#     set_values.add(list(i.values())[0])
# print(set_values)
# Задача 23. Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает кол-во элементов массива, больших предыдущего(элмента с предыдущим номером)
list_1 = [0, -1, 5, 2, 3]
count = 0
for i in range(1, len(list_1)):
    if list_1[i-1] < list_1[i]:
        count += 1
print(count)
