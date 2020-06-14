'''
6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например  название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
'''

goods = []
n = 1
while True:
    question = input('Хотите добавить товар? Введите "да" для добавления или "нет" для выхода из меню добавления '
                     'товаров: ').lower()
    if question == 'да':
        product_full_desc = [n]
        product_specifications = {}
        title = input('Название товара: ').lower()
        price = int(input('Стоимость: '))
        quantity = int(input('Количество: '))
        unit = input('Единица измерения: ').lower()
        product_specifications['название'] = title
        product_specifications['цена'] = price
        product_specifications['количество'] = quantity
        product_specifications['ед'] = unit
        product_full_desc.append(product_specifications)
        product_full_desc = tuple(product_full_desc)
        goods.append(product_full_desc)
        print('Товар успешно добавлен в каталог!')
        n += 1
    elif question == 'нет':
        break
    else:
        print('Неправильная команда')

if goods:
    print('-' * 10)
    print('Текущий каталог товаров:')
    # для более красивого построчного вывода сделаем это через цикл
    for i in goods:
        print(i)
else:
    print('Каталог товаров пуст')

# формируем аналитику товаров
titles = []
prices = []
quantities = []
units = []

for i in range(len(goods)):
    titles.append(goods[i][1].get('название'))
    prices.append(goods[i][1].get('цена'))
    quantities.append(goods[i][1].get('количество'))
    units.append(goods[i][1].get('ед'))

# удаляем возможные дубликаты в списке аналитики о товарах
titles = list(set(titles))
prices = list(set(prices))
quantities = list(set(quantities))
units = list(set(units))

# сортируем списки для упорядоченного отображения в финальном словаре аналитики о товарах
titles.sort()
prices.sort()
quantities.sort()
units.sort()

analytics = {
    'названия': titles,
    'цены': prices,
    'количества': quantities,
    'ед': units
}
print('-' * 10)
print('аналитика о товарах:')
# для более красивого построчного вывода сделаем это через цикл
for key, val in analytics.items():
    print(f'{key}: {val}')
print('-' * 10)