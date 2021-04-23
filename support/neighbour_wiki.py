# Function to adjust the values to SQL Insert
def adv(data):
    a = str(data).replace(",", ".")
    return ''.join(a.split())

import requests
import unidecode
from bs4 import BeautifulSoup
import MySQLdb
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
database = config['database']

db = MySQLdb.connect(host = database['host'],
                     port = int(database['port']),
                     user = database['user'],
                     passwd = database['passwd'])

cur = db.cursor()

url = 'https://pt.wikipedia.org/wiki/Lista_de_bairros_de_Curitiba'
data  = requests.get(url).text
soup = BeautifulSoup(data,"html5lib")

insert = 'INSERT INTO project.data_neighbour (neighbourhood, norm_neighbourhood, area, num_man, num_woman, pop_total, num_houses, mean_revenue_house) VALUES ('
for table in soup.findAll('table',{'class': 'wikitable'}):
    for tr in table.findAll('tr',{'align': 'center'}):
        td = tr.findAll('td')
        neighbourhood = td[0].text.strip()
        norm_neighbourhood = unidecode.unidecode(neighbourhood).upper()
        area = td[1].text.strip()
        num_man = td[2].text.strip()
        num_woman = td[3].text.strip()
        pop_total = td[4].text.strip()
        houses = td[5].text.strip()
        mean_revenue_house = td[6].text.strip()
        sql_insert = insert + '\'' + neighbourhood + '\', \''+ norm_neighbourhood + '\', ' + adv(area) + ', ' + adv(num_man) + ', ' + adv(num_woman) + ', ' + adv(pop_total) + ', ' + adv(houses) + ', ' + adv(mean_revenue_house) + ');'
        cur.execute(sql_insert)
        print(" .")
db.commit()
db.close()
print("Fim!")

