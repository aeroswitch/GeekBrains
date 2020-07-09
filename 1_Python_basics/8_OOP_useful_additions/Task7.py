"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
 методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
  и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a}i'


# adding examples of ComplexNumber class
complex_number_1 = ComplexNumber(2, -1)
complex_number_2 = ComplexNumber(-1, 5)
print(f'Complex number 1:\n{complex_number_1.a} + {complex_number_1.b}i')
print(f'Complex number 2:\n{complex_number_2.a} + {complex_number_2.b}i')
print('*' * 20)
print(f'Sum result:\n{complex_number_1 + complex_number_2}')
print(f'Multiplying result:\n{complex_number_1 * complex_number_2}')

#  -------------------------------------------------------- 7 ----------------------------------------------------------

#
#
# class ComplexNumber:
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.img = imaginary
#
#     def __str__(self):
#         return f'{self.real}+{self.img}i' if self.img > 0 else f'{self.real}{self.img}i'
#
#     def __add__(self, other):
#         return ComplexNumber(self.real + other.real, self.img + other.img)
#
#     def __mul__(self, other):
#         return ComplexNumber((self.real * other.real - self.img * other.img),
#                              (self.img * other.real + self.real * other.img))
#
#
# cn = ComplexNumber(1, -2)
# cn1 = ComplexNumber(3, 4)
# print(cn + cn1)
# print(cn * cn1)
# print(complex(1, -2) * complex(3, 4))  # calculation check