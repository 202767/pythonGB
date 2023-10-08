# Задача 47.
# def transformation(x): return x
# values = [1, 23, 42, 'asdf']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print("OK")
# else:
#     print("Fail")
# Задача 49
# def find_farthest_orbits(orbits):
#     def condition(data): return (data[0] != data[1]) * data[0] * data[1]
#     square_orbits = list(map(condition, orbits))
#     return orbits[square_orbits.index(max(square_orbits))]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbits(orbits))
# Задача 51
# def same_by(characteristics, objects):
#     return len(set(map(characteristics, objects))) in (0, 1)


# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")
