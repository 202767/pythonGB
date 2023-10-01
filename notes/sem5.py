# Задача 31. Последовательность Фибоначчи называется последовательность чисел а0, а1,...аn,...,
# где а0 = 0, а1 = 1, аk = аk-1 + ak-2 (k>1).
# Требуется найти N-е число Фибоначчи
# def fib(n):
#     if n in (0, 1):
#         return n
#     return fib(n-1) + fib(n-2)


# print(fib(int(input("Введите номер числа Фибоначчи: "))))
# n = int(input("Введите номер числа Фибоначчи: "))
# a0, a1 = 0, 1
# for i in range(n):
#     a_next = a0 + a1
#     a0 = a1
#     a1 = a_next
# print(a1)
# Задача 33. Напишите программу, которая заменяет оценки Василия: максимальные на минимальные
# n = int(input("Input amount of marks: "))
# marks = [int(i) for i in input("Input marks: ").split()[:n]]
# print([min(marks) if i == max(marks) else i for i in marks])
# Задача 35. Напишите функцию, котрая принимает одно число и проверяет, является ли оно простым.
# def is_prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#         return True


# print('yes' if is_prime(int(input("Input a number: "))) else 'no')
# Задача 37. Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке (рекурсией)
def rec(n):
    if n == 0:
        return ""
    x = int(input("Введите число: "))
    return rec(n-1) + f" {x}"


n = int(input("Введите количество чисел: "))
print(rec(n))
