"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def is_int(string):
    """Определяет является ли значение внутри строки типом int"""
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_float(string):
    """Определяет является ли значение внутри строки типом float"""
    try:
        float(string)
        return True
    except ValueError:
        return False


def extract_digits(string):
    """Возвращает список значений типа int и float разделенных пробелом из произвольного списка"""
    func_list = []
    for i in string.split():
        if is_int(i):
            i = int(i)
            func_list.append(i)
        elif is_float(i):
            i = float(i)
            func_list.append(i)
    return func_list


def sum_of_digits(input_list):
    """Возвращает сумму значений из произвольного списка"""
    result = 0
    for i in input_list:
        result += i
    return result


digit_list = []

while True:
    user_input = input('Введите числа в одну строку разделяя их пробелом. Для завершения программы введите "Q": ')
    if user_input.find('Q') == 0:
        break
    elif user_input.find('Q') != -1:
        cycle_sum = sum_of_digits(extract_digits(user_input))
        digit_list.append(cycle_sum)
        print(f'сумма всех чисел равна {sum(digit_list)}')
        break
    else:
        cycle_sum = sum_of_digits(extract_digits(user_input))
        digit_list.append(cycle_sum)
        print(f'сумма всех чисел равна {sum(digit_list)}')
