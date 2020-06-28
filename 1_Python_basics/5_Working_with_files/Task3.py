"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
 кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""

import math

with open('text_3.txt', 'r', encoding='utf-8') as f:
    employee_list = f.readlines()
    print(f'Employees who have salary less than 20000:')
    salary = []
    for s in employee_list:
        employee_data = s.strip().split()
        salary.append(float(employee_data[1]))
        if float(employee_data[1]) < 20000:
            print(employee_data[0])
    average_salary = sum(salary) / len(salary)
    print(f'Average salary in the company is: {average_salary}')
