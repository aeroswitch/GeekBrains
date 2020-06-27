"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

result = []

# assign empty dicts, which will be added to the result list
firm_summary = {}
average_profit = {}

with open('text_7.txt', 'r', encoding='utf-8') as f:
    file_content = f.readlines()
    for x in file_content:
        # split each line in the file to the list
        firm = x.strip().split()
        # calculating firm profit using indexes of the list
        firm_profit = int(firm[2]) - int(firm[3])
        # working with 1st dict (firms): assigning firm name as a key and previously calculated profit as a value
        firm_summary[firm[0]] = firm_profit
    # appending created dict to the final list
    result.append(firm_summary)
    print(f'Dict with firms summary:\n{firm_summary}')

    # create list with profits > 0 using created dict, referring to dict values
    profits_list = []
    n = 0
    for profit in list(firm_summary.values()):
        if profit > 0:
            profits_list.append(profit)
            n += 1

    # working with 2nd dict (average profit): assigning average profit as a value
    average_profit['average_profit'] = sum(profits_list) / n
    # appending created dict to the final list
    result.append(average_profit)
    print(f'Dict with average profit:\n{average_profit}')

    print(f'Final list:\n{result}')

# serializing to JSON
with open('text_7.json', 'w', encoding='utf-8') as j:
    # two additional arguments are requested: indent for prettifying JSON and ensure_ascii to show russian letters
    json.dump(result, j, indent=4, ensure_ascii=False)
    print(f'JSON file is created with the following formatting:\n{json.dumps(result, indent=4, ensure_ascii=False)}')




