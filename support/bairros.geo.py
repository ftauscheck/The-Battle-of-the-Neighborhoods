import json
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

with open('bairros.geo.json') as json_file:
    insert = 'INSERT INTO project.geo_neighbour (id, type, name, area, regional_id, regional_name, geometry) VALUES ('
    data = json.load(json_file)
    for f in data['features']:
        id = f['properties']['codigo']
        type =  f['properties']['tipo']
        name=  f['properties']['nome']
        area = f['properties']['area']
        regional_id = f['properties']['codigo_regional']
        regional_name = f['properties']['nome_regional']
        geometry = json.dumps(f['geometry'])
        sql_insert = insert + str(id) + ', \''+ type + '\', \'' + name + '\', ' + str(area) + ', ' + str(regional_id) + ', \'' + regional_name + '\', ST_GeomFromGeoJSON(\'' + geometry + '\'));'
        #print(name)
        #print(geometry)
        cur.execute(sql_insert)
        print(" .")
db.commit()
db.close()