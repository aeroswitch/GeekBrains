"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
 ввода данных свидетельствует пустая строка.
 """

# as guided during webinar, user should be asked to add a string indefinitely until he inputs an empty string

with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        user_str = f.write(input('Write a string to add to the file: '))
        f.write('\n')
        if not user_str:
            break
    print('Content was written to the file text_1.txt')

