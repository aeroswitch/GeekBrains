"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import re

subjects = {}

with open('text_6.txt', 'r', encoding='utf-8') as f:
    content_lines = f.readlines()
    n = 0
    for x in content_lines:
        # we'll use re.findall to calculate the hours in the file in one code line
        hours = [int(x) for x in re.findall('[0-9]+', content_lines[n])]
        # assign a subject as a key and sum of found hours as a value
        subjects[x.strip().split(':')[0]] = sum(hours)
        n += 1
    print(subjects)

# #  -------------------------------------------------------- 6 --------------------------------------------------------
#
#
# mydict = {}
# with open("text_6.txt", encoding="utf-8") as fobj:
#     for line in fobj:
#         name, stats = line.split(':')
#         name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
#         mydict[name] = name_sum
# print(f"{mydict}")
#
# #  ------------------------------------------- вариант решения -------------------------------------------------------
#
#
# with open('text_6.txt', 'r', encoding='utf8') as text_file:
#     a = text_file.readlines()
#     for s in a:
#         new_str = ''.join((i if i in '1234567890' else ' ') for i in s)
#         new_2 = [int(i) for i in new_str.split()]
#         print(f'{s.split()[0]} {sum(new_2)}')
#
# #  ------------------------------------------- вариант решения -------------------------------------------------------
#
#
# with open('text_6.txt', encoding='utf8') as file:
#     my_dict = dict()
#     for line in file:
#         name, other = line.split(": ")
#         for i in other.split():
#             if i != "-":
#                 my_dict[name] = my_dict.get(name, 0) + int(i.split("(")[0])
#
#     print(my_dict)
