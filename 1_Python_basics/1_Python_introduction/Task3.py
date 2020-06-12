# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем
# 3 + 33 + 333 = 369.

user_number = (input('Введите число: '))
one_n = int(user_number)
two_n = int(user_number + user_number)
three_n = int(user_number + user_number + user_number)

result = one_n + two_n + three_n
print(f'Результат: {result}')
