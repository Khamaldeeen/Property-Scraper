import requests 
import pandas as pd 
from bs4 import BeautifulSoup
import time

url = "https://nigeriapropertycentre.com/for-rent/flats-apartments/lagos?bedrooms=3&minprice=300000&maxprice=40000000&q=for-rent+flats-apartments+lagos+3+bedrooms+minprice+300000+maxprice+40000000"
url0 = "https://nigeriapropertycentre.com/for-rent/flats-apartments/lagos/showtype?bedrooms=3&minprice=300000&maxprice=40000000&page="
url1 = "https://nigeriapropertycentre.com/for-rent/flats-apartments/lagos/showtype?bedrooms=3&minprice=300000&maxprice=40000000&page=2"

def scraper(x):
    webpage = requests.get(x)
    refined = BeautifulSoup(webpage.text, 'lxml')
    cards = refined.select('.wp-block')


    Location = []
    for item in cards:
        loc = item.select('.wp-block-content > address > strong')
        for elem in loc:
            splts = elem.get_text().split()
            fin = splts[-2]
            fin = fin.replace(',', '')
            fin = fin.replace('(', '')
            fin = fin.replace(')', '')
            Location.append(fin)

    Prices = []
    for item in cards:
        amt = item.select('.wp-block-content > .pull-sm-left > .price')
        for i, elem in enumerate(amt):
            if i % 2 != 0:
                pri = elem.get('content')
                Prices.append(pri) 


    Features = []
    for item in cards:
        all_ = item.select('.wp-block-footer > .aux-info >li > span')
        items = []
        for elem in all_:
            yuh = elem.get_text()
            items.append(yuh)
        Features.append(' '.join(items))


    Features = Features[2:-2]
    return Location, Features, Prices
#Toilets.pop(0, 1, 23, 24)
#Toilets.pop(0)
#Toilets.pop(21)
#Toilets.pop(21)

urls = [url, url1]
for i in range(3, 50):
    ext = url0 + str(i)
    urls.append(ext)


ML, MF, MP = [], [], []
for item in urls:
    Ml, Mf, Mp = scraper(item)
    ML += Ml
    MF += Mf
    MP += Mp
    time.sleep(4)
    


data = pd.DataFrame({'Location':ML,
                    'Extra Features': MF,
                    'Price': MP})


data.to_csv('3 Bedroom Apart.csv', index=False)



