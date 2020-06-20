"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Реализовать вывод данных о
пользователе одной строкой.
"""


# kwargs!
def fsb(first_name, last_name, birth_date, city, email, phone):
    print(f'Имя: {first_name}, фамилия: {last_name}, год рождения: {birth_date}, город проживания: {city}, '
          f'емейл: {email}, телефон: {phone}')


print('Именованные параметры внутри функции: ')

fsb(last_name='Иванов', first_name='Иван', phone='+7 920 000 0000', city='Рязань', birth_date='1912',
    email='vanyatka@foreveryoung.com')


def fsb_1(**kwargs):
    return kwargs


print('Реализация через **kwargs: ')

print(fsb_1(first_name='Иван', last_name='Иванов', birth_date='1912', city='Рязань', phone='+7 920 000 0000',
            email='vanyatka@foreveryoung.com'))
