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
        # we'll use re.findall to quickly find all the hours in the file
        hours = [int(x) for x in re.findall('[0-9]+', content_lines[n])]
        # assign a subject as a key and sum of found hours as a value
        subjects[x.strip().split(':')[0]] = sum(hours)
        n += 1
    print(subjects)








