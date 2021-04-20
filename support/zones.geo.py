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
x = 1
with open('zones.geo.json') as json_file:
    insert = 'INSERT INTO project.geo_zones (nm_groups, cd_zone, nm_zone, sg_zone, geometry) VALUES ('
    data = json.load(json_file)
    for f in data['features']:
        if f['geometry']['type'] == 'Polygon':
            nm_groups = f['properties']['NM_GRUPO']
            cd_zone =  "" if f['properties']['CD_ZONA'] == None else f['properties']['CD_ZONA']
            nm_zone =  f['properties']['NM_ZONA']
            sg_zone = f['properties']['SG_ZONA']
            geometry = json.dumps(f['geometry'])
            sql_insert = insert + ' \''+ nm_groups + '\', \'' + cd_zone + '\', \'' + nm_zone + '\', \'' + sg_zone + '\', ST_GeomFromGeoJSON(\'' + geometry + '\'));'
            #print(geometry)
            #exit()
            #print(sql_insert)
            print(x)
            cur.execute(sql_insert)
        x = x + 1
db.commit()
db.close()