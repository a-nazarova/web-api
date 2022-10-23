import requests

loc = ['Лондон', 'Шереметьево', 'Череповец']


def get_weather():
    url_template = 'https://ru.wttr.in/{}?nTqM&lang=ru'

    for location in loc:
        url = url_template.format(location)
        response = requests.get(url)
        print(response.text)


get_weather()
