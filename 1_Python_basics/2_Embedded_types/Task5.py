'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
Выполнить без использования .reverse() и sorted()
'''
my_list = [7, 5, 3, 3, 2]
print(f'Изначальный список:\n{my_list}')
new_element = int(input('Введите новый элемент для добавления в список рейтинга: '))
for i in range(len(my_list)):
    if my_list[-1] >= new_element:
        my_list.append(new_element)
        break
    elif my_list[i] < new_element:
        index = i
        my_list.insert(index, new_element)
        break

print(f'Обновленный список:\n{my_list}')

#  -------------------------------------------------------- 5 ----------------------------------------------------------


my_list = [4, 3, 3, 2, 1]

while True:
    print(f"Current rating: {my_list}")
    number = input("Enter rating number or 111 to finish - ")
    if number.lstrip('-').isdigit() and number != "111":
        number = int(number)
        if my_list.count(number):
            my_list.insert(my_list.index(number) + my_list.count(number), float(number))
        else:
            param = 0
            n_param = 0
            for n, i in enumerate(my_list):
                if number > i:
                    if param < i:
                        param = i
                        n_param = n
                else:
                    n_param = n + 1
            my_list.insert(n_param, number)
    elif not number.isdigit():
        print("Enter number please")
    else:
        break

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_list = [9, 8, 7, 7, 7, 6, 5, 3, 3, 3, 2, 1]
new_number = int(input("Введите новый элемент рейтинга в виде натурального числа: "))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
my_list.insert(i, new_number)
print(my_list)

#  ------------------------------------------- вариант решения ---------------------------------------------------------

my_list = [7, 5, 3, 3, 2]

n = int(input('количество ввода: '))
for it in range(n):
    number = int(input('введите рейтинг: '))
    i = 0
    for val in my_list:
        if number > val:
            break
        i += 1
    my_list.insert(i, float(number))
    print(my_list)