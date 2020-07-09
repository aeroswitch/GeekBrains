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

#  -------------------------------------------------------- 1 ----------------------------------------------------------


# class Data:
#     def __init__(self, day_month_year):
#         self.day_month_year = str(day_month_year)
#
#     @classmethod
#     def extract(cls, day_month_year):
#         my_date = []
#
#         for i in day_month_year.split():
#             if i != '-': my_date.append(i)
#         return int(my_date[0]), int(my_date[1]), int(my_date[2])
#
#     @staticmethod
#     def valid(day, month, year):
#
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2019 >= year >= 0:
#                     return f'Всё в порядке'
#                 else:
#                     return f'Неправильный год'
#             else:
#                 return f'Неправильный месяц'
#         else:
#             return f'Неправильный день'
#
#     def __str__(self):
#         return f'Текущая дата {Data.extract(self.day_month_year)}'
#
#
# today = Data('24 - 02 - 2020')
# print(today)
# print(Data.valid(11, 13, 2022))
# print(today.valid(26, 10, 2020))
# print(Data.extract('11 - 11 - 2011'))
# print(today.extract('24 - 02 - 2020'))
# print(Data.valid(24, 11, 2020))

#  ------------------------------------------- вариант решения ---------------------------------------------------------

#
# class OwnError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# class Date(object):
#
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         is_date = cls.is_date_valid(date_as_string)
#         try:
#             if is_date == False:
#                 raise OwnError("Wrong date!")
#         except OwnError as err:
#             print(err)
#             return
#
#         day, month, year = map(int, date_as_string.split('-'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         return day <= 31 and month <= 12 and year <= 3999
#
#
# date2 = Date.from_string('11-10-2012')
#
# try:
#     print(date2.day, date2.month, date2.year)
# except:
#     print('OOps. Something wrong')


#  ------------------------------------------- вариант решения ---------------------------------------------------------

# class Data:
#     def __init__(self, data):
#         self.data = data
#
#     @classmethod
#     def change_type(cls, data):
#         return f'День {int(data[0]):02d}, Месяц {int(data[1]):02d}, Год {int(data[2])}'
#
#     @staticmethod
#     def validation(data):
#         if not int(data[0]) in range(1, 32) or not int(data[1]) in range(1, 13) or int(data[2]) > 2020:
#             return 'Введена некоррекная дата!'
#
#     def data_func(self):
#         result_1 = Data.change_type(self.data.split('-'))
#         result_2 = Data.validation(self.data.split('-'))
#         return result_2 if result_2 else f'Переформатированная дата (тип int)\n{result_1}'
#
#
# user_data = input('Введите дату (чч-мм-гг): ')
# mc = Data(user_data)
# print(mc.data_func())
# user_data = input('Введите дату (чч-мм-гг): ')
# mc_2 = Data(user_data)
# print(mc_2.data_func())
# print(mc.data_func())