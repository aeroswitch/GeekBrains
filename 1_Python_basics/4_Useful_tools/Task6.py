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