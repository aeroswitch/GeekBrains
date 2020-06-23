"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

import random

# creating a list with pseudo random numbers
random_list = []
for x in range(0, 15):
    n = random.randint(0, 15)
    random_list.append(n)

print(f'Original list:\n{random_list}')

new_list = [x for x in random_list if random_list.count(x) == 1]
print(f'Updated list:\n{new_list}')
