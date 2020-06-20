"""
Реализовать функцию my_func() , которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""


def my_func(x, y, z):
    numbers = [x, y, z]
    numbers.remove(min(numbers))
    return sum(numbers)


print(my_func(-4, 500, 13.6))
