"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income_dict['wage']


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return income_dict['wage'] + income_dict['bonus']


income_dict = {'wage': 55555, 'bonus': 33333}


test_worker_1 = Position('Raskin', 'Bobbins', 'ice cream maker')
test_worker_2 = Position('Jack', 'Daniels', 'bartender')
test_worker_3 = Position('Dalt', 'Winsey', 'entertainer')

print(f'{test_worker_1.get_full_name()}, {test_worker_1.position}, total income: {test_worker_1.get_total_income()}')
print(f'{test_worker_2.get_full_name()}, {test_worker_2.position}, total income: {test_worker_2.get_total_income()}')
print(f'{test_worker_3.get_full_name()}, {test_worker_3.position}, total income: {test_worker_3.get_total_income()}')