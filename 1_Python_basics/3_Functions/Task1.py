"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(var_1, var_2):
    """Принимает два числа и возвращает результат их деления"""
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        return


print('Реализация через input в вызове функции: ')
print(division(float(input('Введите делимое: ')), float(input('Введите делитель: '))))


# способ 2
def division_2():
    """Принимает два числа и возвращает результат их деления"""
    try:
        var_1 = float(input('Введите делимое: '))
        var_2 = float(input('Введите делитель: '))
        return var_1 / var_2
    except ZeroDivisionError:
        return


print('Реализация через input в теле функции: ')
print(division_2())
