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
cur.execute("USE project;")

url = 'https://pt.wikipedia.org/wiki/Lista_de_bairros_de_Curitiba'
data  = requests.get(url).text
soup = BeautifulSoup(data,"html5lib")

insert = 'INSERT INTO project.data_neighbour (neighbourhood, norm_neighbourhood, area, men, women, total, households, avg_income) VALUES ('
for table in soup.findAll('table',{'class': 'wikitable'}):
    for tr in table.findAll('tr',{'align': 'center'}):
        td = tr.findAll('td')
        neighbourhood = td[0].text.strip()
        norm_neighbourhood = unidecode.unidecode(neighbourhood).upper()
        area = td[1].text.strip()
        men = td[2].text.strip()
        women = td[3].text.strip()
        total = td[4].text.strip()
        households = td[5].text.strip()
        avg_income = td[6].text.strip()
        sql_insert = insert + '\'' + neighbourhood + '\', \''+ norm_neighbourhood + '\', ' + adv(area) + ', ' + adv(men) + ', ' + adv(women) + ', ' + adv(total) + ', ' + adv(households) + ', ' + adv(avg_income) + ');'
        cur.execute(sql_insert)
        print(" .")

db.commit()
# In case of duplicity of neighbourhood, delete the second one:
sql_delete = 'DELETE t1 FROM project.data_neighbour t1 INNER JOIN project.data_neighbour t2 WHERE t1.id < t2.id AND t1.norm_neighbourhood = t2.norm_neighbourhood;'
cur.execute(sql_delete)

db.commit()
db.close()
print("Fim!")

