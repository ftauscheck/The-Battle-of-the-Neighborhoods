def return_circle(azimuth_step, radius, lat, long):
    lat = math.radians(lat)
    long = math.radians(long)
    temp_content=""
    azimuth = 0
    lat0 = 0
    long0 = 0
    while azimuth < 360:
        point = {}
        tc = math.radians(azimuth)
        temp_lat = math.degrees(math.asin(math.sin(lat)*math.cos(radius) + math.cos(lat)*math.sin(radius)*math.cos(tc)))
        if math.cos(long) == 0 :
            temp_lon = math.degrees(long)
        else:
            temp_lon = math.degrees(((long + math.asin(math.sin(tc)*math.sin(radius) / math.cos(lat)) + math.pi) % (2*math.pi)) - math.pi)

        if azimuth == 0:
            lat0 = temp_lat
            long0 = temp_lon
        if temp_content == "":
            temp_content = 'LINESTRING(' + str(round(temp_lon, 6)) + " " + str(round(temp_lat,6))
        else:
            temp_content = temp_content + ", " + str(round(temp_lon, 6)) + " " + str(round(temp_lat,6))
        azimuth += azimuth_step
    return temp_content +', '+ str(round(long0, 6)) + " " + str(round(lat0,6)) +')'

import MySQLdb
import psycopg2
import configparser
import math
from geopy import distance

config = configparser.ConfigParser()
config.read('config.ini')
database = config['database']
database2 = config['postgis']

mysql = MySQLdb.connect(host = database['host'],
                     port = int(database['port']),
                     user = database['user'],
                     passwd = database['passwd'])

cur_mysql = mysql.cursor()

conn_string = "host='"+ database2['host'] +"' user='" + database2['user'] + "' password='"+ database2['passwd']+"'"
psql = psycopg2.connect(conn_string)
cur_psql = psql.cursor()

azimuth_step = 5 
hexagon_apothem = 1 # km
radius = 1/distance.EARTH_RADIUS

cur_mysql.execute('SELECT id, name, lat, `long`, address, categories, tipCount, tier, rating, likes, verified FROM project.foursquare_venues')
x = 0
for record in cur_mysql:
    id = record[0]
    name = record[1]
    lat = record[2]
    long = record[3]
    address = record[4]
    categories = record[5]
    tipCount = record[6]
    tier = record[7]
    rating = record[8]
    likes = record[9]
    verified = record[10]
    area = return_circle(azimuth_step, radius, lat, long)
    sql_insert = 'INSERT INTO project.foursquare_venues (id, name, lat, long, geo_point, address, categories, tipCount, tier, rating, likes, verified, area) VALUES (%s, %s, %s, %s, CAST(ST_SetSRID(ST_Point(%s, %s), 4326) AS geometry), %s, %s, %s, %s, %s, %s, %s, CAST(ST_SetSRID(ST_MakePolygon( ST_GeomFromText(%s)), 4326) AS geometry));'
    cur_psql.execute(sql_insert, (id, name, lat, long, long, lat, address, categories, tipCount, tier, rating, likes, verified, area))
    x += 1
psql.commit()
print("Migrados {} venues...".format(x))