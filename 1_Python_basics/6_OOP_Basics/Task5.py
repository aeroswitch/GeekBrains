"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Starting drawing')


class Pen(Stationery):
    def draw(self):
        print(f'Starting drawing with {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Starting drawing with {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Starting drawing with {self.title}')


pen_example = Pen('pen')
pen_example.draw()

pencil_example = Pencil('pencil')
pencil_example.draw()

handle_example = Handle('handle')
handle_example.draw()
