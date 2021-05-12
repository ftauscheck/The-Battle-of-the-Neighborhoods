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
with open('support/GeoJSON/Curitiba_main_streets.geojson', encoding='utf-8') as json_file:
    insert = 'INSERT INTO project.geo_main_streets (code, name, status, sub_system, geometry) VALUES ('
    data = json.load(json_file)
    for f in data['features']:
        if f['geometry']['type'] == 'LineString':
            code = 'NULL' if f['properties']['CODVIA'] == None else '\'' + str(db.escape_string(f['properties']['CODVIA']), 'utf-8') + '\''
            name =  'NULL' if f['properties']['NMVIA'] == None else '\'' + str(db.escape_string(f['properties']['NMVIA']), 'utf-8') + '\''
            status=  f['properties']['STATUS']
            sub_system = f['properties']['SIST_VIARI']
            geometry = json.dumps(f['geometry'])
            sql_insert = insert + code + ', ' + name + ', \'' + str(db.escape_string(status), 'utf-8') + '\', \'' + str(db.escape_string(sub_system), 'utf-8') + '\', ST_SwapXY(ST_GeomFromGeoJSON(\'' + geometry + '\')));'
            cur.execute(sql_insert)
        x = x + 1

print('Main Streets - INSERT {}'.format(x))
db.commit()
db.close()