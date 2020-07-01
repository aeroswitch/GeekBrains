"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

# Let's ask user to set up upper limit of factorial calculation

user_number = int(input('Specify a max number for calculating factorial: '))
print('Error! Integer value is expected')


def factorial(n):
    """Returns a factorial of the specified number"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fact_generator(n):
    """Returns a generator that consists of selected range of numbers factorials"""
    for x in range(1, n + 1):
        yield factorial(x)


# check the final result
print(f'Factorials of numbers from 1! to {user_number}! are:')
for el in fact_generator(user_number):
    print(el)
# #  -------------------------------------------------------- 7 ----------------------------------------------------------
#
# from itertools import count
# from math import factorial
#
#
# def fact_gen():
#     for el in count(1):
#         yield factorial(el)
#
#
# generator = fact_gen()
# x = 0
# for i in generator:
#     if x == 15:
#         break
#     else:
#         x += 1
#         print(f"Factorial {x} = {i}")
#
#
# #  ------------------------------------------- вариант решения ---------------------------------------------------------
#
#
# def fact_gen(n):
#     m = 1
#     for i in range(1, n):
#         if i > 15:
#             break
#         m *= i
#         yield m
#
#
# for i in fact_gen(26):
#     print(i)