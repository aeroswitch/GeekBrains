"""2. Реализовать проект расчета суммарного расхода ткани на производстве одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
 соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
 классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class Clothing(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    # calculate total tissue consumption via __add__ method overload
    def __add__(self, other):
        return self.tissue_consumption_calculation() + other.tissue_consumption_calculation()


class Coat(Clothing):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 76:
            self.__size = 76
        elif size > 121:
            self.__size = 121
        else:
            self.__size = size

    def tissue_consumption_calculation(self):
        return int(self.size / 6.5 + 0.5)


class Suit(Clothing):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 158:
            self.__height = 158
        elif height > 218:
            self.__height = 218
        else:
            self.__height = height

    def tissue_consumption_calculation(self):
        return int(self.height * 2 + 0.3)


burberry = Coat(600)
print(f'Added Class object Coat with size parameter of size 600. Limitation defined by setter converted '
      f'it to {burberry.size}')
print(f'Result of calculation for tissue consumption is {burberry.tissue_consumption_calculation()}')

saint_laurent = Suit(100)
print(f'Added Class object Suit with height parameter of size 100. Limitation defined by setter converted '
      f'it to {saint_laurent.height}')
print(f'Result of calculation for tissue consumption is {saint_laurent.tissue_consumption_calculation()}')


print(f'Total tissue consumption of both objects is {burberry + saint_laurent}')
