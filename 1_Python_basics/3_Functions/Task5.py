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

#  -------------------------------------------------------- 5 ----------------------------------------------------------


def sum_num():
    s = 0
    while True:
        in_list = input("Enter a number, input 'q' to exit: ").split()
        for num in in_list:
            if num == "q":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("To exit the program, enter - 'q'.")
        print(f"Sum of numbers = {s}")


print(sum_num())

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def summary():
    result = 0
    while True:
        print(f"Текущая сумма = {result}")
        input_s = input("Введите строку чисел, разделенных пробелом для подсчета суммы (# - символ для завершения): ").split()
        for value in input_s:
            if value == "#":
                print(f"Окончательная сумма = {result}")
                break
            try:
                result += float(value)
            except ValueError:
                print(f"Значение {value} не было учтено при подсчете суммы - неверный тип")
        else:
            # если символа завершения программы не были то продолжаем ввод данных
            continue
        # сюда мы дойдем только если встретим символ завершения программы
        break
    return f"Окончательная сумма = {result}"

summary()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


num = 0
try:
    while num != '#':
        for i in map(int, input("Для выхода наберите '#'\nВведите числа, используя пробел.\n").split()):
            num += i
        print(num)
except ValueError:
    print(num)