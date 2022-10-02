import requests

city = input('Введите название города: ')
url = 'https://wttr.in/{city}'
weather = requests.get(url)
print(weather.text)