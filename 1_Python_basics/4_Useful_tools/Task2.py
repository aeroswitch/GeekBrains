"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

import random

# creating a list with pseudo random numbers
random_list = []
for x in range(0, 15):
    n = random.randint(0, 150)
    random_list.append(n)

print(f'Original list:\n{random_list}')

# let's use zip() with [1:] slice for second list to get a neighbour elements for comparison
new_list = [e2 for e1, e2 in zip(random_list, random_list[1:]) if e2 > e1]
print(f'Updated list:\n{new_list}')

# #  -------------------------------------------------------- 2 ----------------------------------------------------------
#
#
# my_list = [15, 16, 2, 3, 1, 7, 5, 4, 10]
# more_than = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
# print(more_than)
