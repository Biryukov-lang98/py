import config
import telebot
import requests
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot(config.token)
URL = 'https://sinoptik.com.ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80'
HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

def get_content(html):
  global t_min, t_max  

    soup = BS(html, 'html.parser')
    items = soup.select('div', "#sinoptik-app > div.wrapper > main > div.weather__content > div.weather__content_tabs.clearfix > div.weather__content_tab.current")
    
    for item in items.select('.weather__content_tab-temperature'):
        t_min =  item.select(' .min')[0].text
        t_max =  item.select(' .max')[0].text

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAPVXzhJJKFCT57XCdefUFPNnOhKt8wAAq8AAwLV8A_J6qM7HY_gzxoE')
    bot.send_message(message.chat.id, 'Какой город вас интересует?')

@bot.message_handler(content_types=['text'])

def send_text(message):
    
    if message.text == 'Краснодар':
        bot.send_message(message.chat.id, 'Погода в Краснодаре: ' + t_min + t_max)


bot.polling()

    








