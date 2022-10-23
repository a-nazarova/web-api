import requests

url_template = 'https://ru.wttr.in/{}'
url = url_template.format('Москва', 'svo', 'Череповец')
response = requests.get(url)
print(response.text)
