import requests
from bs4 import BeautifulSoup
from django.apps import apps
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CrawlingPractice.settings")
import django
django.setup()
from testApp.models import melonList

iamhuman = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}




def melonCrolling():
    url = "https://www.melon.com/chart/day/index.htm"
    req = requests.get(url,headers = iamhuman)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    songs = []
    artists = []
    albums = []
    ranks = []
    images = []

        
    song = soup.find_all('div', {"class":"ellipsis rank01"})
    for i in song:
        songs.append(i.find('a').text)
    artist = soup.find_all('div',{"class":"ellipsis rank02"})
    for k in artist:
        artists.append(k.find('a').text)
    rank = soup.find_all('span',{"class":"rank"})
    for m in rank[1:]:
        ranks.append(m.text)
    albumName = soup.find_all('div',{"class":"ellipsis rank03"})
    for j in albumName:
        albums.append(j.find('a').text)
    albumCover = soup.select('.image_typeAll > img')
    for k in albumCover:
        images.append(k.get('src'))
    sumlist = list(zip(ranks,songs,artists,images))
    return sumlist

if __name__ == '__main__':
    Melon_data_list = melonCrolling()
    melonList.objects.all().delete()
    for i in range(len(Melon_data_list)):
        melonList(
            rank=int(Melon_data_list[i][0]),
            songName = Melon_data_list[i][1],
            singerName = Melon_data_list[i][2],
            imgSrc = Melon_data_list[i][3],
        ).save()


#copy selector => lst50 > td:nth-child(4) > div > a > img