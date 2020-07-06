"""3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление
(__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n*****."""


class Cell:
    def __init__(self, cell_quantity):
        self.cell_quantity = int(cell_quantity)

    def __add__(self, other):
        return self.cell_quantity + other.cell_quantity

    def __sub__(self, other):
        if self.cell_quantity >= other.cell_quantity:
            return (self.cell_quantity - other.cell_quantity)
        else:
            return 'quantity of cells in second object should be higher than in first object'

    def __mul__(self, other):
        return self.cell_quantity * other.cell_quantity

    def __truediv__(self, other):
        return int(self.cell_quantity / other.cell_quantity)

    def make_order(self, digit):
        result = ''
        for n in range(self.cell_quantity):
            if n % digit == 0:
                result += '\n'
            result += '*'
        return result


cell_1 = Cell(15)
cell_2 = Cell(2)

print(f'Sum: {cell_1 + cell_2}')
print(f'Sub: {cell_1 - cell_2}')
print(f'Mul: {cell_1 * cell_2}')
print(f'Div: {cell_1 / cell_2}')
print(cell_1.make_order(4))



# #  -------------------------------------------------------- 3 --------------------------------------------------------
#
#
# class Cell:
#     def __init__(self, nums):
#         self.nums = nums
#
#     def make_order(self, rows):
#         return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)
#
#     def __str__(self):
#         return self.nums
#
#     def __add__(self, other):
#         return f'Sum of cell is: {self.nums + other.nums}'
#
#     def __sub__(self, other):
#         return self.nums - other.nums if self.nums - other.nums > 0 \
#             else "Ячеек в первой клетке меньше равно второй, вычитание невозможно!"
#
#     def __mul__(self, other):
#         return f'Multiply of cells is: {self.nums * other.nums}'
#
#     def __truediv__(self, other):
#         return f'Truediv of cells is: {round(self.nums / other.nums)}'
#
#
# cell_1 = Cell(15)
# cell_2 = Cell(24)
# print(cell_1 + cell_2)
# print(cell_1 - cell_2)
# print(cell_1 * cell_2)
# print(cell_1 / cell_2)
# print(cell_2.make_order(7))
