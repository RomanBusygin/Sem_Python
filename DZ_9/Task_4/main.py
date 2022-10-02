import requests

bot = '5699740380:AAH8f6hNtBnCs_-fqN9e7WOB94FNBgkwJdA'
city = input('Введите название города: ')
url_text = f'https://wttr.in/{city}?M'
url_png = f'https://wttr.in/{city}_0pM.png'
weather_text = requests.get(url_text)
weather_png = requests.get(url_png)
print(weather_text.text)

with open(r'C:\Users\Roman\Desktop\GEEK\Block_2\Phyton\DZ\DZ_9\Task_4\imag.png', 'wb') as file:
    file.write(weather_png.content)
    
requests.get(f'https://api.telegram.org/bot{bot}/sendPhoto', params = dict(chat_id = '864101142'), files = {'photo': open('imag.png', 'rb')})