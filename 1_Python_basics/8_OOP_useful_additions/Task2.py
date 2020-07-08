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
