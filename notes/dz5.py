# задача 1
# def f(a, b):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     else:
#         return a * f(a, b-1)
#
# a = 3
# b = 5
# print(f(a, b))
# задача 2
def sum(a, b):
    if b == 0:
        return a
    elif b < 0:
        return sum(a - 1, b + 1)
    elif b > 0:
        return sum(a + 1, b - 1)


a = -3
b = 5
print(sum(a, b))
