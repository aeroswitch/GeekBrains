'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
 необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
'''

user_str = input('Введите строку из нескольких слов разделенных пробелами: ')

result = user_str.split()
for ind, el in enumerate(result, 1):
    print(f'{ind}) {el[:10]}')
