# задача 1
# distance_a_day = int(input("Введите кол-во км, пройденное за день: "))
# distance = int(input("Введите кол-во км, пройденное за всё время: "))
# print(
#    f"Необходмое кол-во дней - {(distance_a_day + distance - 1) // distance}")

# задача 2
# a = int(input('Введите количество учеников в первом классе:'))
# b = int(input('Введите количество учеников во втором классе:'))
# c = int(input('Введите количество учеников в третьем классе:'))
# sum1 = a//2 + a % 2
# sum2 = b//2 + b % 2
# sum3 = c//2 + c % 2
# print(sum1 + sum2 + sum3)

# задача 3
# i = int(input("В какой вагон сел Витя: "))
# j = int(input("Какой вагон указан на табличке: "))
# if i == j:
#    print("Нужна дополнительная информация! ")
# else:
#    print(i + j - 1)

# задача 4
""" 
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')
 """
# задача 9
""" 
num = int(input("Введите число: "))
result = 1
for nums in range(1, num + 1, 1):
    result *= nums
print(result)
 """
# задача 11
""" 
num = int(input("Введите число: "))
first_fib = 0
second_fib = 1
i = 2
while second_fib < num:
    next_fib = first_fib + second_fib
    first_fib = second_fib
    second_fib = next_fib
    i += 1
    if second_fib > num:
        i = -1
print(i)
"""
# задача 15
# num = int(input("Введите кол-во арбузов: "))
# mass = int(input("Введите массу арбуза: "))
# max_mass = mass
# min_mass = mass
# for i in range(num - 1):
#     mass = int(input("Введите массу арбуза: "))
#     if max_mass < mass:
#         max_mass = mass
#     elif min_mass > mass:
#         min_mass = mass
# print(min_mass, max_mass)
# задача 13
num = int(input("Введите кол-во дней: "))
count = 0
max_count = 0
for i in range(num):
    temp = int(input("Введите температуру: "))
    if temp >= 0:
        count += 1
        if max_count < count:
            max_count = count
    else:
        count = 0
print(max_count)
