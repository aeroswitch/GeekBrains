"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
 вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
  ситуацию и не завершиться с ошибкой."""


class OwnError(Exception):
    def __init__(self, text):
        self.text = text


try:
    user_input = int(input('Specify a number for denominator x in the equation "100 / x": '))
    if user_input == 0:
        raise OwnError('Error! Can\'t divide by 0')
except ValueError:
    print('Error! This is not a number')
except OwnError as error:
    print(error)
else:
    print(f'Result: {round(100 / user_input, 1)}')


#  -------------------------------------------------------- 2 ----------------------------------------------------------

# class MyZeDiEr(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# def div(s_1, s_2):
#     try:
#         s_1, s_2 = int(s_1), int(s_2)
#         if s_2 == 0:
#             raise MyZeDiEr("Division by zero forbidden!!!")
#         return round(s_1 / s_2, 3)
#     except ValueError:
#         return "Value Error"
#     except MyZeDiEr as my:
#         return my
#
#
# print(div(input("Enter first number - "), input("Enter first second - ")))


#  ------------------------------------------- вариант решения ---------------------------------------------------------


# class MyDivisionZeroError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# div = lambda x, y: x / y if y != 0 else MyDivisionZeroError('Ошибка дедения на 0!!')
#
# print(div(1, 0))
#
# print(div(4, 2))
