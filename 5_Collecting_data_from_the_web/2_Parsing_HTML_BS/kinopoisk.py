from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

# https://www.kinopoisk.ru/popular/films/?quick_filters=serials&tab=all

main_link = 'https://www.kinopoisk.ru'

params = {
    'quick_filters': 'serials',
    'tab': 'all'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.121 Safari/537.36'
}

response = requests.get(main_link + '/popular/films/', params=params, headers=headers)
soup = bs(response.text, 'html.parser')

serials_list = soup.find_all('div', {'class': 'desktop-rating-selection-film-item'})
serials = []

for serial in serials_list:
    serial_data = {}
    serial_name = serial.find('p')
    serial_link = main_link + serial_name.parent['href']
    serial_name = serial_name.getText()  # отличие метода .getText от метода .text заключается в том, что .getText
    # будет искать всех детей и внуков и правнуков и т.д., а .text только детей
    serial_genre = serial.find_all('span', {'class': 'selection-film-item-meta__meta-additional-item'})[-1].text
    serial_rating = serial.find('span', {'class': 'rating__value'}).text
    try:
        serial_rating = float(serial_rating)
    except:
        serial_rating = None

    serial_data['name'] = serial_name
    serial_data['link'] = serial_link
    serial_data['genre'] = serial_genre
    serial_data['rating'] = serial_rating
    serials.append(serial_data)

pprint(serials)
