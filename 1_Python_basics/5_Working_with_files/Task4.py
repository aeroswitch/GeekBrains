"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

from googletrans import Translator

file_translate = Translator()
numbers = []

with open('text_4.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    print(f'Current file content: {content}')
    for x in content:
        elements = x.strip().split()
        numbers.append(elements[0])

print(f'Numbers to translate: {numbers}')

with open('text_4_RU.txt', 'w+', encoding='utf-8') as r:
    n = 0
    for y in range(0, 4):
        # we'll use Google translator for converting EN numbers to RU numbers
        r.write(file_translate.translate(numbers[n], dest='ru').text)
        r.write(' - ')
        r.write(str(n + 1))
        r.write('\n')
        n += 1
    r.seek(0)
    print(f'New file with translated content: {r.readlines()}')
