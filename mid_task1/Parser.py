import json

import requests
from config import FILM_URL, HEADERS
from bs4 import BeautifulSoup
import re

class Parser():
    months = [
        'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
    ]

    html = ''

    film_list = []
    
    def __init__(self, url):
        response = requests.get(url, headers=HEADERS)
        self.html = response


    def img_to_date(self, imgs):
        #Возможно, имело смысл это оформить покрасивее, вынести повторяющийся код в отдельный статический метод.
        #Не знаю, насколько это критично
        if len(imgs) == 2:
            day = imgs[0]['src'].split('/')[5]
            day = re.findall('\d+', day)
            month = imgs[1]['src'].split('/')[5]
            month = re.findall('\d+', month)
            return str(day[0] + ' ' + self.months[int(month[0]) - 1])
        elif len(imgs) == 3:
            dec = imgs[0]['src'].split('/')[5]
            dec = re.findall('\d+', dec)
            day = imgs[1]['src'].split('/')[5]
            day = re.findall('\d+', day)
            month = imgs[2]['src'].split('/')[5]
            month = re.findall('\d+', month)
            return str(dec[0] + day[0] + ' ' + self.months[int(month[0]) - 1])


    def get_html(self, url):
        response = requests.get(url, headers=HEADERS)
        return response


    def parse(self):
        html = self.html
        soup = BeautifulSoup(html.text, features='html.parser')
        items = soup.find('div', class_='prem_list')
        films = items.find_all('div', class_='premier_item')
        for film in films:
            print(film.text)

            name = film.find('span', class_="name_big").text #Здесь получили название на русском
            name_eng = film.find_all('span')[1].text #Здесь получили название на английском
            film_link = FILM_URL + film.find('a').get('href') #Получили ссылку на фильм
            film_id = film_link.split('/')[4]

            try:
                votes = film.find('span', id='rating_' + film_id).find('u').find('b').text
                film_rating = film.find('span', id='rating_' + film_id).find('u').text
            except:
                votes = ' '
                film_rating = ' '



'''            company = film.find('s', class_='company').text #Получили компанию
            dates = film.find('div', class_='day').find_all('img')
            date = self.img_to_date(dates) #Дата премьеры
            genres = film.find('div', class_='textBlock').find_all('span')[3].text.split(',') #Жанры

            self.film_list.append({
                film_id: {
                    'name': name,
                    'name_eng': name_eng.split('(')[0].replace("  ", ""),
                    'film_link': film_link,
                    'film_rating': film_rating.replace(u'\xa0', u' ').split(' ')[0],
                    'votes': votes.replace(u'\xa0', u' '),
                    'date': date,
                    'company': company,
                    'genres': genres
                }
            })
            self.save_json(self.film_list)

    def save_json(self, list):
        with open('films.json', 'w') as f:
            json.dump(list, f, indent=4)'''




