# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# n = int(input("Введите кол-во элементов первого множества: "))
# m = int(input("Введите кол-во элементов второго множества: "))
# set_1 = set()
# set_2 = set()
# for i in range(n):
#     i = int(input("Введите элемент первого множества: "))
#     set_1.add(i)
# for j in range(m):
#     j = int(input("Введите элемнт второго множества: "))
#     set_2.add(j)
# print(*set_1.intersection(set_2))
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
n = int(input("Введите количество кустов на грядке: "))
list_1 = []
for i in range(n):
    list_1.insert(i, int(input("Введите количество ягод на кусту: ")))
print(list_1)
sum = 0
for j in range(-1, n-1, 1):
    if list_1[j] + list_1[j-1] + list_1[j+1] > sum:
        sum = list_1[j] + list_1[j-1] + list_1[j+1]
print(sum)