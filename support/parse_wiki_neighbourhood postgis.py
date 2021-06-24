# Function to adjust the values to SQL Insert
def adv(data):
    a = str(data).replace(",", ".")
    return ''.join(a.split())

import requests
import unidecode
from bs4 import BeautifulSoup
import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
database = config['postgis']

conn_string = "host='"+ database['host'] +"' user='" + database['user'] + "' password='"+ database['passwd']+"'"
db=psycopg2.connect(conn_string)

cur = db.cursor()
cur.execute("TRUNCATE project.data_neighbourhood;")
cur.execute("ALTER SEQUENCE project.data_neighbourhood_id_seq RESTART WITH 1;")

url = 'https://pt.wikipedia.org/wiki/Lista_de_bairros_de_Curitiba'
data  = requests.get(url).text
soup = BeautifulSoup(data,"html5lib")

for table in soup.findAll('table',{'class': 'wikitable'}):
    for tr in table.findAll('tr',{'align': 'center'}):
        td = tr.findAll('td')
        neighbourhood = td[0].text.strip()
        norm_neighbourhood = unidecode.unidecode(neighbourhood).upper()
        area = adv(td[1].text.strip())
        men = adv(td[2].text.strip())
        women = adv(td[3].text.strip())
        total = adv(td[4].text.strip())
        households = adv(td[5].text.strip())
        avg_income = adv(td[6].text.strip())
        sql_insert = 'INSERT INTO project.data_neighbourhood (neighbourhood, norm_neighbourhood, area, men, women, total, households, avg_income) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
        cur.execute(sql_insert, (neighbourhood, norm_neighbourhood, area, men, women, total,households, avg_income))
        print(" .")

db.commit()
# In case of duplicity of neighbourhood, delete the second one:
sql_delete = 'DELETE FROM project.data_neighbourhood t1 WHERE t1.id > (SELECT MIN(t2.id) FROM project.data_neighbourhood t2 WHERE t1.norm_neighbourhood = t2.norm_neighbourhood);'
cur.execute(sql_delete)

db.commit()
db.close()
print("Fim!")

