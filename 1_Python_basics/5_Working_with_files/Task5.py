"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
 подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

with open('text_5.txt', 'w+') as f:
    random_list = random.sample(range(1, 15), 5)
    print(f'Source list with random list: {random_list}')
    # writing the list to the file
    for x in random_list:
        f.write(str(x))
        f.write(' ')
    # return the pointer to the beginning of the file and read the content
    f.seek(0)
    content = f.readlines()
    n = 0
    result = 0
    # reading the content as numbers and calculating their sum
    for x in content:
        numbers = x.strip().split()
    for y in numbers:
        result = result + int(numbers[n])
        n += 1

    print(f'Sum of all the numbers in the file is {result}')

# #  -------------------------------------------------------- 5 --------------------------------------------------------
#
#
# from random import randint
#
# sum_el = 0
# with open("text.txt", "w", encoding="utf-8") as my_file:
#     for i in range(100):
#         el = randint(1, 100)
#         sum_el += el
#         my_file.write(str(el) + " ")
#
# print(f"Sum of elements - {sum_el}")
#
# #  ------------------------------------------- вариант решения -------------------------------------------------------
#
#
# from random import randint
#
# num_str = " ".join([str(randint(1, 1000)) for _ in range(100000)])
# with open('task_5_file.txt',  mode='w+', encoding='utf-8') as the_file:
#     the_file.write(num_str)
#     the_file.seek(0)
#     print(sum(map(int, the_file.readline().split())))
