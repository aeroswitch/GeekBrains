# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

num = int(input('Введите целое положительное число: '))
max_num = 0

if num < 10:
    max_num = num
elif num == 10:
    max_num = 1

while num > 10:
    check_num = num % 10
    if check_num == 9:
        max_num = 9
        break
    elif check_num > max_num:
        max_num = check_num
    num = num // 10
print(f'Самое большое число в цифре: {max_num}')
