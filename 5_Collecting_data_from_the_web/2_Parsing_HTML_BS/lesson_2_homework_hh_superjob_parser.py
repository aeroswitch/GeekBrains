"""Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы) с сайтов
Superjob и HH. Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы).
Получившийся список должен содержать в себе минимум:
Наименование вакансии.
Предлагаемую зарплату (отдельно минимальную, максимальную и валюту).
Ссылку на саму вакансию.
Сайт, откуда собрана вакансия.
По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение). Структура должна быть
 одинаковая для вакансий с обоих сайтов.
"""

from bs4 import BeautifulSoup as bs
import requests
import unicodedata
import re
from pprint import pprint

# https://hh.ru/search/vacancy?clusters=true&enable_snippets=true&search_field=name&text=аналитик&L_save_area=true
# &area=1&showClusters=true

main_link_hh = 'https://hh.ru'

vacancy_search_phrase = input('Insert search phrase for require vacancy: ')

params = {
    'clusters': 'true',
    'enable_snippets': 'true',
    'search_field': 'name',
    'text': vacancy_search_phrase,
    'L_save_area': 'true',
    'area': '1',
    'showClusters': 'true'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.121 Safari/537.36'
}

response = requests.get(main_link_hh + '/search/vacancy', params=params, headers=headers)

vacancies = []
# define markers for handling various salary grouping in the cycle below
min_salary_marker = 'от'
max_salary_marker = 'до'
fork_salary_marker = '-'

# introduce counter for showing page parsing progress
n = 1

# outer cycle for parsing next page (pagination)
while True:
    soup = bs(response.text, 'html.parser')
    vacancies_list = soup.find_all('div', {'data-qa': ['vacancy-serp__vacancy vacancy-serp__vacancy_premium',
                                                       'vacancy-serp__vacancy']})
    print(f'Parsing page {n} from hh.ru...')
    # inner cycle for parsing vacancy data
    for vacancy in vacancies_list:
        vacancy_data = {}
        vacancy_name = vacancy.find('a')
        vacancy_link = vacancy_name['href']
        vacancy_name = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-title'}).text
        try:
            vacancy_salary = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).text
            vacancy_salary = unicodedata.normalize('NFKD', vacancy_salary)
            vacancy_salary_currency = (re.sub('[^рубUSD]', '', vacancy_salary)).upper()
            if min_salary_marker in vacancy_salary:
                vacancy_salary_min = float(re.sub('\D+', '', vacancy_salary))
                vacancy_salary_max = None
            elif max_salary_marker in vacancy_salary:
                vacancy_salary_max = float(re.sub('\D+', '', vacancy_salary))
                vacancy_salary_min = None
            elif fork_salary_marker in vacancy_salary:
                vacancy_salary_fork = re.sub('[рубUSD\.]', '', vacancy_salary)
                vacancy_salary_min = float(re.split('-', vacancy_salary_fork)[0].replace(' ', ''))
                vacancy_salary_max = float(re.split('-', vacancy_salary_fork)[1].replace(' ', ''))
        except:
            vacancy_salary = None
            vacancy_salary_min = None
            vacancy_salary_max = None
            vacancy_salary_currency = None
        vacancy_employer = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'})
        try:
            vacancy_employer_link = main_link_hh + vacancy_employer['href']
        except:
            vacancy_employer_link = None
        try:
            vacancy_employer = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}).text
        except:
            vacancy_employer = None
        vacancy_publish_date = vacancy.find('span', {'class': 'vacancy-serp-item__publication-date'}).text
        vacancy_publish_date = unicodedata.normalize('NFKD', vacancy_publish_date)
        vacancy_data['name'] = vacancy_name
        vacancy_data['link'] = vacancy_link
        vacancy_data['salary_min'] = vacancy_salary_min
        vacancy_data['salary_max'] = vacancy_salary_max
        vacancy_data['salary_currency'] = vacancy_salary_currency
        vacancy_data['employer'] = vacancy_employer
        vacancy_data['employer_link'] = vacancy_employer_link
        vacancy_data['publish_date'] = vacancy_publish_date
        vacancy_data['source'] = 'hh.ru'
        vacancies.append(vacancy_data)

    # check if next page exists
    next_page_marker = soup.find('a', {'data-qa': 'pager-next'})
    if not next_page_marker:
        break
    # if exists then get new page for parsing
    response = requests.get(main_link_hh + next_page_marker['href'], headers=headers)
    n += 1
    print()

pprint(vacancies)
pprint(f'Done! Total amount of parsed vacancies: {len(vacancies)}')
