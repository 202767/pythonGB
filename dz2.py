# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# heads = 0
# tails = 0

# num = int(input("Input amount of coins: "))
# for i in range(num):
#     elem = int(input("Input side of the coin: "))
#     if elem == 0:
#         heads += 1
#     elif elem == 1:
#         tails += 1
# if heads > tails:
#     print(f"You should rotate {tails} coin(s)")
# else:
#     print(f"You should rotate {heads} coin(s)")
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# s = int(input("Input sum of nums: "))
# p = int(input("Input multiplication of nums: "))
# if s * s - 4 * p >= 0:
#     x1 = (s-int((s**2-4*p)**0.5))//2
#     x2 = (s+int((s**2-4*p)**0.5))//2
#     if x1 > 0 and x2 > 0:
#         print(f"Nums are: {x1} {x2}")
#     else:
#         print("There are no such natural nums")
# else:
#     print("There are no such natural nums")
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# n = int(input("Input a num: "))
# k = 1
# while k < n:
#     print(k, end=' ')
#     k = k * 2
