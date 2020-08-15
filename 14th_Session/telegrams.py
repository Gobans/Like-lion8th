import telegram, requests, os
from bs4 import BeautifulSoup
import schedule
import datetime
import time

now = datetime.datetime.now()
bot = telegram.Bot(token='1151221612:AAHeURxGMmWB_tLsZoKV34dNk95-Ddnnc2o')
# bot.sendMessage(chat_id = 957744248)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def telegram_bot():
    url = "https://algumon.com/"
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.select('div.post-group > div.product-body.clearfix > div > p:nth-child(2) > span > a')
    latest = name[0].text.strip()
    latest_link = "https://algumon.com"+str(name[0].attrs['href'])
    print(latest)
    with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+', encoding="utf-8") as f_read:
        before = f_read.readline()
        if before != latest :
            bot.sendMessage(chat_id=957835890, text="현재 최저가 상품명은 다음과 같아요 \n"+latest+'\n'+latest_link)
        else :
            bot.sendMessage(chat_id=957835890, text="현재 최저가 상품명은 다음과 같아요 \n"+latest+'\n'+latest_link)
        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+', encoding="utf-8") as f_write:
        f_write.write(latest)
        f_write.close()
        
telegram_bot()

seconds =0
while(True):
    telegram_bot()
    time.sleep(5)
    seconds += 5
    if seconds == 30:
        break