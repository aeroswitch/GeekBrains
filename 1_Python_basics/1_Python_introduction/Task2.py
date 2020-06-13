# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_seconds = int(input('Введите кол-во секунд: '))

hours = user_seconds // 3600
minutes = (user_seconds // 60) - (hours * 60)
seconds = user_seconds - (minutes * 60) - (hours * 3600)

print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
