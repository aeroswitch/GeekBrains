"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, init_matrix):
        self.init_matrix = init_matrix

    def __str__(self):
        for row in range(len(self.init_matrix)):
            for column in range(len(self.init_matrix[row])):
                print(f'{self.init_matrix[row][column]:6d}', end='')
            print()
        # I don't like using empty string as a return value, but I don't see how to use return in cycle. We could
        # somehow append values to some list in cycles and return the list, but the representation will be incorrect
        return ''

    def __add__(self, other):
        # define a list that would show final matrix and define an empty row, which will be appended to a final matrix
        result_matrix = []
        result_matrix_row = []
        for row in range(len(self.init_matrix)):
            for column in range(len(self.init_matrix[row])):
                # here we calculate a sum of elements in each column of the first row
                result_matrix_row.append(self.init_matrix[row][column] + other.init_matrix[row][column])
            # once done - append sum of element of each column as a separate row
            result_matrix.append(result_matrix_row)
            # here we need to reset result_matrix_row because in cycle we will need to calculate this row again until
            # all the rows are iterated in the cycle
            result_matrix_row = []
            # in the return, we need to convert result_matrix into object of Matrix class
        return Matrix(result_matrix)


# checking with example
matrix_1 = Matrix([[46, 54, 33, 12], [-6, 128, 1, 8], [-14, 15, 18, -8]])
print('Matrix 1:')
print(matrix_1)

matrix_2 = Matrix([[7, -14, 20, 4], [8, -1, 0, 3], [-22, 44, 22, 1]])
print('Matrix 2:')
print(matrix_2)

print(f' Sum of two matrices is:')
print(matrix_1 + matrix_2)

# #  -------------------------------------------------------- 1 --------------------------------------------------------
#
#
# class Matrix:
#
#     def __init__(self, data):
#         self.data = data
#
#     def __str__(self):
#         return '\n'.join('\t'.join([str(itm) for itm in line]) for line in self.data)
#
#     def __add__(self, other):
#         try:
#             m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
#                  for line in range(len(self.data))]
#             return Matrix(m)
#         except IndexError:
#             return f'Ошибка размерностей матриц'
#
#
# m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
# m_2 = [['5', '7', '23'], ['9', '23', '-54'], ['12', '3', '16']]
#
# mtrx_1 = Matrix(m_1)
# mtrx_2 = Matrix(m_2)
# new_m = mtrx_1 + mtrx_2
#
# print(mtrx_1)
# print('#' * 30)
# print(mtrx_2)
# print('#' * 30)
# print(mtrx_1 + mtrx_2)
# print('#' * 30)
# print(new_m)
# m_3 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
# m_4 = [['5', '7', '23'], ['9', '-54'], ['12', '3', '16']]
# print('#' * 30)
# mtrx_3 = Matrix(m_3)
# mtrx_4 = Matrix(m_4)
# print(mtrx_3 + mtrx_4)
# print('#' * 30)
# m_3 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
# m_4 = [['5', '7', '23'], ['12', '3', '16'], ['12', '3']]
# print(mtrx_3 + mtrx_4)
#

# #  ------------------------------------------- вариант решения -------------------------------------------------------
#
#     a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
#     b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]
#
#
#     class Matrix:
#         def __init__(self, lists):
#             self.lists = lists
#
#         def __str__(self):
#             return '\n'.join(map(str, self.lists))
#
#         def __add__(self, other):
#             c = []
#             for i in range(len(self.lists)):
#                 c.append([])
#                 for j in range(len(self.lists[0])):
#                     c[i].append(self.lists[i][j] + other.lists[i][j])
#             return '\n'.join(map(str, c))
#
#
#     matrix_1 = Matrix(a)
#     matrix_2 = Matrix(b)
#     print(f"Matrix 1\n{matrix_1}\n{'-'*20}")
#     print(f"Matrix 2\n{matrix_2}\n{'-'*20}")
#     print(f"matrix 1 + matrix 2\n{matrix_1 + matrix_2}")
#
# #  ------------------------------------------- вариант решения -------------------------------------------------------
#
#
# class Matrix(object):
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __str__(self):
#         return str('\n '.join(['\t '.join([str(i) for i in j]) for j in self.matrix]))
#
#     def __add__(self, other):
#         return Matrix([self.matrix[i][j] + other.matrix[i][j] for i in range(len(self.matrix))]
#                       for j in range(len(self.matrix[0])))
#
#
# stroki = int(input("Введите количество строк и столбцов матрицы: "))
# stolbci = stroki
#
# matrix1 = Matrix([[i * j for j in range(stroki)] for i in range(stolbci)])
# matrix2 = Matrix([[i + j for j in range(stroki)] for i in range(stolbci)])
#
# print('First matrix:\n', matrix1, end='\n\n')
# print('Second matrix:\n', matrix2, end='\n\n')
# print('Summ of first and second matrix:\n', matrix1 + matrix2)
#
# #  ------------------------------------------- вариант решения -------------------------------------------------------
#
#
# class Matrix:
#
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __str__(self):
#         return '\n'.join(map(lambda r: '   '.join(map(str, r)), self.matrix)) + '\n'
#
#     def __add__(self, other):
#         return Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))
#
#
# my_m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# my_m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(my_m1)
# print(my_m2)
# s = my_m1 + my_m2
# print(s)