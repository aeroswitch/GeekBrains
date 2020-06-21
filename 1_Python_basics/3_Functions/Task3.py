"""
Реализовать функцию my_func() , которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""


def my_func(x, y, z):
    numbers = [x, y, z]
    numbers.remove(min(numbers))
    return sum(numbers)


print(my_func(-4, 500, 13.6))

#  -------------------------------------------------------- 3 ----------------------------------------------------------


def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return "Enter only a numbers!"


print(my_func(2, 11, -30))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def my_func(arg1, arg2, arg3):
    return sum(sorted([arg1, arg2, arg3])[1:])


print(my_func(1978, 1, 2))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_func = lambda arg_1, arg_2, arg_3: (arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)

print(my_func(8, 7, 9))