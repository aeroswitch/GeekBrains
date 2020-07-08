"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
 месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def extracting_date_as_int(cls):
        dd_mm_yy_as_numbers = str(cls('10-13-20').str_date).split('-')
        return [int(x) for x in dd_mm_yy_as_numbers]

    @staticmethod
    def validating_date_format():
        if Date.extracting_date_as_int()[0] > 31 or Date.extracting_date_as_int()[0] < 1:
            return 'dd should be in range 01-31'
        elif Date.extracting_date_as_int()[1] > 12 or Date.extracting_date_as_int()[1] < 1:
            return 'mm should be in range 01-12'
        elif Date.extracting_date_as_int()[2] > 30 or Date.extracting_date_as_int()[2] < 5:
            return 'yy should be in range 05-30'
        else:
            return 'validation finished successfully'


# check if methods work
print(f'List of converted numbers:\n{Date.extracting_date_as_int()}')
print(f'validation result:\n{Date.validating_date_format()}')
