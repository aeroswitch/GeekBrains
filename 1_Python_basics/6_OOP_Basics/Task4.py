"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и
WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""
# skipping all try / excepts and other error handling code to save time

import random

direction_options = ['left', 'right']


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is moving!')

    def stop(self):
        print(f'{self.name} has stopped')

    def turn(self, direction=random.choice(direction_options)):
        print(f'{self.name} has turned {direction}')

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed} km/h')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Speed limit for {self.name} is violated! Max speed is 60 km/h')
        else:
            print(f'Current speed of {self.name} is {self.speed} km/h')


class SportCar(Car):
    def __init__(self, color, name, speed=220, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Speed limit for {self.name} is violated! Max speed is 40 km/h')
        else:
            print(f'Current speed of {self.name} is {self.speed} km/h')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


print('*' * 50)
# test TownCar class
print('Town car: ')
town_car_example = TownCar(35, 'black', 'Skoda')
print(f'{town_car_example.name}\'s color is {town_car_example.color}')
town_car_example.go()
town_car_example.turn()
town_car_example.show_speed()
town_car_example.speed = 50
print(f'{town_car_example.name} is accelerating to {town_car_example.speed} km/h!')
town_car_example.show_speed()
town_car_example.speed = 70
print(f'{town_car_example.name} is accelerating to {town_car_example.speed} km/h!')
town_car_example.show_speed()
print('*' * 50)

# test SportCar class
print('Sport car: ')
sport_car_example = SportCar('Red', 'Ferrari')
print(f'{sport_car_example.name}\'s color is {sport_car_example.color}')
sport_car_example.go()
sport_car_example.turn()
sport_car_example.show_speed()
print('*' * 50)

# test WorkCar class
print('Work car: ')
work_car_example = WorkCar(25, 'grey', 'Gazel')
print(f'{work_car_example.name}\'s color is {work_car_example.color}')
work_car_example.go()
work_car_example.turn()
work_car_example.show_speed()
work_car_example.speed = 50
print(f'{work_car_example.name} is accelerating to {work_car_example.speed} km/h!')
work_car_example.show_speed()
print('*' * 50)

# test PoliceCar class
print('Police car: ')
police_car_example = PoliceCar(60, 'black', 'Ford')
print(f'{police_car_example.name}\'s color is {police_car_example.color}')
police_car_example.go()
police_car_example.turn()
police_car_example.show_speed()
police_car_example.speed = 80
print(f'{police_car_example.name} is accelerating to {police_car_example.speed} km/h!')
police_car_example.show_speed()
print(police_car_example.is_police)
print('*' * 50)

# #  -------------------------------------------------------- 4 --------------------------------------------------------
#
# class Car:
#     ''' Автомобиль '''
#
#     def __init__(self, name, color, speed, is_police=False):
#         self.name = name
#         self.color = color
#         self.speed = speed
#         self.is_police = is_police
#         print(f'Новая машина: {self.name} (цвет {self.color}) машина полицейская - {self.is_police}')
#
#     def go(self):
#         print(f'{self.name}: Машина поехала.')
#
#     def stop(self):
#         print(f'{self.name}: Машина остановилась.')
#
#     def turn(self, direction):
#         print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}.')
#
#     def show_speed(self):
#         return f'{self.name}: Скорость автомобиля: {self.speed}.'
#
#
# class TownCar(Car):
#     ''' Городской автомобиль '''
#
#     def show_speed(self):
#         return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
#             if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"
#
#
# class WorkCar(Car):
#     ''' Грузовой автомобиль '''
#
#     def show_speed(self):
#         return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
#             if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"
#
#
# class SportCar(Car):
#     ''' Спортивный автомобиль '''
#
#
# class PoliceCar(Car):
#     ''' Полицейский автомобиль '''
#
#     def __init__(self, name, color, speed, is_police=True):
#         super().__init__(name, color, speed, is_police)
#
#
# police_car = PoliceCar('"Полицайка"', 'белый', 80)
# police_car.go()
# print(police_car.show_speed())
# police_car.turn(0)
# police_car.stop()
# print()
#
# work_car = WorkCar('"Грузовичок"', 'хаки', 40)
# work_car.go()
# work_car.turn(1)
# print(work_car.show_speed())
# work_car.turn(0)
# work_car.stop()
#
# print()
# sport_car = SportCar('"Спортивка"', 'красный', 120)
# sport_car.go()
# sport_car.turn(0)
# print(sport_car.show_speed())
# sport_car.stop()
# print()
#
# town_car = TownCar('"Малютка"', 'жёлтый', 50)
# town_car.go()
# town_car.turn(1)
# town_car.turn(0)
# print(town_car.show_speed())
# town_car.stop()
#
# print(f'\nМашина {town_car.name} (цвет {town_car.color})')
# print(f'Машина {police_car.name} (цвет {police_car.color})')