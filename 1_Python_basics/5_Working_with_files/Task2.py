"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества
слов в каждой строке.
"""

with open('text_1.txt', 'r+', encoding='utf-8') as f:
    f.read()
    # add few new strings to the existing file from Task 1
    f.write('Adding a text string to the end of the file\n')
    f.write('Adding another one\n')
    # after 'write' operation, the pointer will be located at the end of the file, so need to return it to the start
    f.seek(0)
    print(f'Quantity of strings in the file text_1.txt: {len(f.readlines())}')
    # returning pointer again
    f.seek(0)
    strings = f.readlines()
    n = 1
    print('Quantity of words in each string: ')
    for w in strings:
        w = len(w.strip().split())
        print(f'string #{n}: {w}')
        n += 1

# #  -------------------------------------------------------- 2 -------------------------------------------------------
#
#
# counter = 0
# with open("text_2.txt", "r", encoding='utf-8') as f_obj:
#     for line in f_obj:
#         counter += 1
#         line_words = line.split()
#         print(line, 'Длина строки: ', len(line_words))
#     print('Всего строк: ', counter)
#
# #  ------------------------------------------- вариант решения ------------------------------------------------------
#
#
# with open("text_2.txt", encoding='utf-8') as f:
#     my_line = f.readlines()
#     for index, value in enumerate(my_line, 1):
#         number_of_words = len(value.split())
#         print(f'Строка {index} содержит {number_of_words} слов')