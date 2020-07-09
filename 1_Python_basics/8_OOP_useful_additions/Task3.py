"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
 скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
 очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
 Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
 При этом работа скрипта не должна завершаться.
"""


class OwnError(Exception):
    def __init__(self, text):
        self.text = text


numbers_list = []
while True:
    try:
        user_input = input('Specify a number to append to the list (or type "stop" to quit): ')
        if user_input == 'stop':
            print('Script was stopped by user')
            break
        elif not user_input.isdigit():
            raise OwnError('Error! You should specify a number, not a string')
    except OwnError as error:
        print(error)
        continue
    numbers_list.append(int(user_input))

print(f'Result list: {numbers_list}')

#  -------------------------------------------------------- 3 ----------------------------------------------------------


# class OwnError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# my_list = []
#
# while True:
#     inp_data = input("Введите число: ")
#     if inp_data == "":
#         break
#     try:
#         if inp_data.isdigit():
#             my_list.append(int(inp_data))
#         else:
#             raise OwnError("введено не число")
#     except OwnError as err:
#         print(err)
#         continue
#
# print(my_list)

#  ------------------------------------------- вариант решения ---------------------------------------------------------

#
# class MyList:
#     print_list = []
#
#     # Попробуем сделать исключение как класс в классе..
#     @staticmethod
#     class NotFloatExcept(Exception):
#         def __init__(self, txt):
#             self.txt = txt
#
#     # Проверим что вновь введенная строка является числом, если да, перобразуем к числовому типу
#     def __is_float(self, input_str):
#         is_one_dot, is_one_minus = 0, 0
#         for i in input_str:
#             if ord(i) >= 48 and ord(i) <= 57:
#                 pass
#             # В числе может быть одн точка
#             elif ord(i) == 46 and is_one_dot == 0:
#                 is_one_dot += 1
#             # А еще минус
#             elif ord(i) == 45 and is_one_minus == 0:
#                 is_one_minus += 1
#             else:
#                 raise self.NotFloatExcept('Введенная строка не является числом!')
#
#         #  Если число целое, так и вернем
#         if is_one_dot == 0:
#             return int(input_str)
#         return float(input_str)
#
#     # Добавляем новое число в список
#     def __call__(self, new_str):
#         try:
#             self.print_list.append(self.__is_float(new_str))
#         except self.NotFloatExcept as e:
#             print(e)
#
#     # Выводим на печать
#     def __str__(self):
#
#         return str(self.print_list)[1:-1]
#
#
# list = MyList()
#
# while True:
#     print('Введите число: ', end='')
#     n = input()
#     if n == '':
#         print('Окончание программы')
#         break
#     else:
#         list(n)
#         print(list)