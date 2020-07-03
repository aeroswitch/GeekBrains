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
