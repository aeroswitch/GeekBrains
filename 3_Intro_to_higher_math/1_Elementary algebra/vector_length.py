import math


def calculate_vector_length_plane(x, y):
    # вычисляет длину вектора на плоскости
    return math.sqrt(x ** 2 + y ** 2)


def calculate_vector_length_space(x, y, z):
    # вычисляет длину вектора в пространстве
    return math.sqrt(x ** 2 + y ** 2 + z ** 2)


print(f'Длина вектора на плоскости равна: {calculate_vector_length_plane(2, 5)}')
print(f'Длина вектора в пространстве равна: {calculate_vector_length_space(2, 5, 5)}')
