"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

# the task is designed to be ran via terminal as requirements say to create scripts (assuming running via terminal?)
# 3 parameters are expected: 1) script name; 2) starting number for the first iterator; 3) quantity of iterations for
# the second iterator

import sys
import itertools

# first iterator
try:
    user_number = int(sys.argv[1])
except ValueError:
    print('Incorrect parameter. Integer is expected')


def iterator_1_1():
    for el in itertools.count(user_number):
        if el > 30:
            break
        else:
            yield el


# checking the result
print('Generating integer numbers starting from the specified one:')
try:
    for x in iterator_1_1():
        print(x)
except NameError:
    print('Error: starting number was not specified correctly')

# second iterator

user_list = [1, 2, 5, 13, 255, 2246]

try:
    user_iteration_number = int(sys.argv[2])
except ValueError:
    print('Incorrect parameter. Integer is expected')


def iterator_2_1():
    n = 0
    for z in itertools.cycle(user_list):
        if n > user_iteration_number:
            break
        n += 1
        yield z


# checking the result
print(f'Repeating the elements of original list: {user_list} {user_iteration_number} times: ')
try:
    for a in iterator_2_1():
        print(a)
except NameError:
    print('Error: starting number was not specified correctly')

# #  -------------------------------------------------------- 6 ----------------------------------------------------------
#
#
# from itertools import count, cycle
#
# print('Программа генерирует целые числа, начиная с указанного. Для генерации следующего числа необходимо нажать Enter,'
#       ' для выхода из программы - "q"')
# for i in count(int(input('Введите стартовое число: '))):
#     print(i, end='')
#     quit = input()
#     if quit == 'q':
#         break
#
# print(
#     'Программа повторяет элементы списка. Для генерации следующего повторения необходимо нажать Enter, для выхода'
#     ' из программы - "q"')
# u_list = input('Введите список, разделяя элементы пробелом: ').split()
# iter = cycle(u_list)
# quit = None
#
# while quit != 'q':
#     print(next(iter), end='')
#     quit = input()
#
# #  ------------------------------------------- вариант решения ---------------------------------------------------------
#
#
# from itertools import islice, cycle, count
#
#
# def unexpected(start_el, stop_el, num_str):
#     try:
#         start_el, stop_el, num_str = int(start_el), int(stop_el), int(num_str)
#         my_list = [el for el in islice(count(), start_el, stop_el + 1)]
#         #  repeat_list = [next(cycle(my_list)) for el in range(num_str)]
#         r_list = iter(el for el in cycle(my_list))
#         repeat_list = [next(r_list) for _ in range(num_str)]
#         print(my_list)
#         return repeat_list
#     except ValueError:
#         return "Value Error"
#     except TypeError:
#         return "TypeError"
#
#
# print(unexpected(input("List starting at - "), input("from to - "), input("Number of repetition - ")))
#
# #  ------------------------------------------- вариант решения ---------------------------------------------------------
#
#
# from itertools import count, cycle
#
# progr_lang = list(input("Введите через пробел ТОП 5 языков программирования: ").split())
#
# # создаем бесконечный итератор из списка языков программирования введенным пользователем
# iter = cycle(progr_lang)
#
# # выводим с помощью итератора count с ограничением, чтобы не уйти в бесконечный цикл
# for n in count():
#     if n > 10:
#         break
#     else:
#         print(f"{n} - {next(iter)}")