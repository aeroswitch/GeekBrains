"""
1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, записывающую собранные
 вакансии в созданную БД.
2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы.
3. Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта.
"""

import requests
import unicodedata
import re
from pprint import pprint
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient


class Scrapper():

    def __init__(self, mongodb_client, database, collection):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/85.0.4183.121 Safari/537.36'
        }

        self.main_link_hh = 'https://hh.ru'
        self.main_link_superjob = 'https://www.superjob.ru'

        self.mongodb = MongoClient(mongodb_client)
        self.database = self.mongodb[database]
        self.collection = self.database[collection]

    def parsing_vacancies_hh(self, vacancy_search_phrase):
        params_hh = {
            'clusters': 'true',
            'enable_snippets': 'true',
            'search_field': 'name',
            'text': vacancy_search_phrase,
            'L_save_area': 'true',
            'area': '1',
            'showClusters': 'true'
        }

    


params_superjob = {
    'keywords': vacancy_search_phrase,
    'geo%5Bt%5D%5B0%5D': '4'
}

vacancies = []
response = requests.get(main_link_hh + '/search/vacancy', params=params_hh, headers=headers)

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
            if vacancy_salary_currency == 'РУБ':
                vacancy_salary_currency = 'RUR'
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
        vacancy_data['name'] = vacancy_name
        vacancy_data['link'] = vacancy_link
        vacancy_data['salary_min'] = vacancy_salary_min
        vacancy_data['salary_max'] = vacancy_salary_max
        vacancy_data['salary_currency'] = vacancy_salary_currency
        vacancy_data['employer'] = vacancy_employer
        vacancy_data['employer_link'] = vacancy_employer_link
        vacancy_data['source'] = 'hh.ru'
        vacancies.append(vacancy_data)

    # check if next page exists
    next_page_marker = soup.find('a', {'data-qa': 'pager-next'})
    if not next_page_marker:
        break
    # if exists then get new page for parsing
    response = requests.get(main_link_hh + next_page_marker['href'], headers=headers)
    n += 1

vacancies_parsed_from_hh = len(vacancies)
response = requests.get(main_link_superjob + '/vacancy/search/', params=params_superjob, headers=headers)

fork_salary_marker = '—'
agreement_salary_marker = 'По договорённости'
exact_salary_marker = '/'
n = 1

while True:
    soup = bs(response.text, 'html.parser')
    vacancies_list = soup.find_all('div', {'class': ['Fo44F QiY08 LvoDO']})

    print(f'Parsing page {n} from superjob.ru...')
    # inner cycle for parsing vacancy data
    for vacancy in vacancies_list:
        vacancy_data = {}
        vacancy_name = vacancy.find('div', {'class': ['_3mfro PlM3e _2JVkc _3LJqf']})
        vacancy_link = main_link_superjob + vacancy_name.findChildren(recursive=False)[0]['href']
        vacancy_name = vacancy.find('div', {'class': ['_3mfro PlM3e _2JVkc _3LJqf']}).text
        vacancy_salary = vacancy.find('span', {'class': '_1OuF_ _1qw9T f-test-text-company-item-salary'}).text
        vacancy_salary = unicodedata.normalize('NFKD', vacancy_salary)
        vacancy_employer = vacancy.find('span', {'class': '_3mfro _3Fsn4 f-test-text-vacancy-item-company-name _9fXTd '
                                                          '_2JVkc _2VHxz _15msI'})
        try:
            vacancy_employer_link = main_link_superjob + vacancy_employer.findChildren(recursive=False)[0]['href']
        except:
            vacancy_employer_link = None
        try:
            vacancy_employer = vacancy_employer.text
        except:
            vacancy_employer = None
        if vacancy_salary == 'По договорённости':
            vacancy_salary_currency = None
            vacancy_salary_min = None
            vacancy_salary_max = None
        elif min_salary_marker in vacancy_salary:
            vacancy_salary_min = re.sub('\D+', '', vacancy_salary)
            vacancy_salary_max = None
            vacancy_salary_currency = (re.sub('[^рубUSD]', '', vacancy_salary)).upper()
            if vacancy_salary_currency == 'РУБ':
                vacancy_salary_currency = 'RUR'
        elif max_salary_marker in vacancy_salary and agreement_salary_marker not in vacancy_salary:
            vacancy_salary_max = re.sub('\D+', '', vacancy_salary)
            vacancy_salary_min = None
            vacancy_salary_currency = (re.sub('[^рубUSD]', '', vacancy_salary)).upper()
            if vacancy_salary_currency == 'РУБ':
                vacancy_salary_currency = 'RUR'
        elif fork_salary_marker in vacancy_salary:
            vacancy_salary_fork = re.sub(' ', '', vacancy_salary)
            vacancy_salary_min = re.split('—', vacancy_salary_fork)[0]
            vacancy_salary_max = re.split('—', vacancy_salary_fork)[1].replace('руб./месяц', '')
            vacancy_salary_currency = (re.sub('[^рубUSD]', '', vacancy_salary)).upper()
            if vacancy_salary_currency == 'РУБ':
                vacancy_salary_currency = 'RUR'
        elif exact_salary_marker in vacancy_salary:
            vacancy_salary_min = re.sub('\D+', '', vacancy_salary)
            vacancy_salary_max = vacancy_salary_min

        vacancy_data['name'] = vacancy_name
        vacancy_data['link'] = vacancy_link
        vacancy_data['salary_min'] = vacancy_salary_min
        vacancy_data['salary_max'] = vacancy_salary_max
        vacancy_data['salary_currency'] = vacancy_salary_currency
        vacancy_data['employer'] = vacancy_employer
        vacancy_data['employer_link'] = vacancy_employer_link
        vacancy_data['source'] = 'superjob.ru'
        vacancies.append(vacancy_data)

    # check if next page exists
    next_page_marker = soup.find('a', {'class': 'icMQ_ _1_Cht _3ze9n f-test-button-dalshe f-test-link-Dalshe'})
    if not next_page_marker:
        break
    # if exists then get new page for parsing
    response = requests.get(main_link_superjob + next_page_marker['href'], headers=headers)
    n += 1

pprint(vacancies)
pprint(f'Done! Total amount of parsed vacancies: {len(vacancies)}. Vacancies parsed from hh.ru:'
       f' {vacancies_parsed_from_hh}, vacancies parsed from superjob.ru: {len(vacancies) - vacancies_parsed_from_hh}')
