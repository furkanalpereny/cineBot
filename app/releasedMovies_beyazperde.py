# All rights reserved by Furkan Alperen Yildirim
# cineBot is a bot which is posting informations about actual movies.

from bs4 import BeautifulSoup
import requests
import datetime
from app import getImages
import os
import json

class movie(object):
    def __init__(self):
        self.title = ""
        self.actor = ""
        self.director = ""
        self.date = ""
        self.time = ""
        self.subject = ""
        self.content = ""
        self.imgLink = ""
        #self.imgLocalPath = ""


def soup(link):
    r = requests.get(link) #request.get aracılığıyla site içeriği çekildi
    soup = BeautifulSoup(r.content, "html.parser") #html parse edildi

    return soup


def dateToLink():
    link = "http://www.beyazperde.com/filmler/takvim/week-" #sonuna tarih eklenecek link
    link = link + str(getNextSaturday()) #linkin sonuna getnextsaturday methodundan dönen string eklendi

    return link


def getNextSaturday():
    today = datetime.date.today() #bugünün tarihi
    saturday = today + datetime.timedelta((5-today.weekday()) % 7) #içinde bulunulan haftanın cumartesi gününü hesaplıyor

    return str(saturday)


def getMoviesThisWeek():
    movies = []
    link = str(dateToLink())
    print(link)
    gelenVeri = soup(link).find_all('div', attrs={'class': 'col-left'}) #html filtreleme
    gelenVeri = gelenVeri[0].find_all("ul")
    gelenVeri = gelenVeri[0].find_all("li", attrs={'class': 'mdl'})

    for i in gelenVeri:
        m_obj = movie()

        # pull title
        try:
            a = i.find_all("a", attrs={'class': 'meta-title-link'})
            title = a[0].text 
            m_obj.title = title
        except:
            m_obj.title = None

        # pull date-time-subject
        try:
            a = i.find_all(
                "div", attrs={'class': 'meta-body-item meta-body-info'})
            spacer = a[0].text.replace("\n", "")
            spacer = spacer.split("/") # / charına göre string split edildi
            m_obj.date = spacer[0]
            m_obj.time = spacer[1].strip() #baş ve sondaki boşluklar filtrelendi
            m_obj.subject = spacer[2].replace(" ", "") #boşluklar filtrelendi
        except:
            m_obj.date = None
            m_obj.time = None
            m_obj.subject = None

        # pull directors
        try:
            a = i.find_all(
                "div", attrs={'class': 'meta-body-item meta-body-direction light'})
            director = a[0].find_all("span")
            directors = []
            for j in director:
                directors.append(j.text)
            director = ', '.join(map(str, directors)) #arraydaki verileri aralarına virgül koyarak stringe çevirir
            m_obj.director = director
        except:
            m_obj.director = None

        # pull actors
        try:
            a = i.find_all(
                "div", attrs={'class': 'meta-body-item meta-body-actor light'})
            actor = a[0].find_all("span")
            actors = []
            for j in actor:
                actors.append(j.text)
            actor = ', '.join(map(str, actors))
            m_obj.actor = actor
        except:
            m_obj.actor = None

        # pull content
        try:
            a = i.find_all("div", attrs={'class': 'content-txt'})
            content = a[0].text
            m_obj.content = content.strip() #baş ve sondaki boşluklar filtrelendi
        except:
            m_obj.content = None

        # pull img
        try:
            a = i.find_all(
                "div", attrs={'class': 'card entity-card entity-card-list cf'})
            img = a[0].find_all("figure")
            img = img[0].find_all("img")[0]
            img = str(img)
            img = img.split('"')
            for i in img:
                if 'http' in i:
                    img = i.replace("/c_215_290", "") #linkteki 215*290 filtresi kaldırılıyor
                    break

            m_obj.imgLink = img
            path = 'src/img/'+getNextSaturday()+'/'
            #m_obj.imgLocalPath = getImages.saveImage(img, path)
            m_obj.imgLocalPath = None
        except:
            m_obj.imgLink = None
            #m_obj.imgLocalPath = None

        movies.append(m_obj.__dict__)

    writeMoviesToJson(movies)
    return movies

def writeMoviesToJson(movies):
    filePath = "src/json/"
    jsonPath = filePath+getNextSaturday()+"_releasedMovies.json"

    if not os.path.exists(filePath): #eğer öyle uzantıda dosya yoksa dosya oluşturur
        os.makedirs(filePath)
    with open(jsonPath, 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=4) #film dict'i json'a dump ediliyor



