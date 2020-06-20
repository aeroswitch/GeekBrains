"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


# посмотреть как работает склеивание ''.join(sentence).split()

def int_func(word):
    word = list(word)
    if 96 < ord(word[0]) < 123:
        word[0] = chr(ord(word[0]) - 32)
    word = ''.join(word)
    return word


def capital_sentence():
    sentence = list(input('Введите строку из слов состоящих из латинских букв нижнего регистра. Слова разделите '
                          'пробелами: '))
    sentence = ''.join(sentence).split()
    print(sentence)
    x = 0
    for i in sentence:
        i = int_func(i)
        sentence[x] = i
        x += 1
    return sentence


print(capital_sentence())
