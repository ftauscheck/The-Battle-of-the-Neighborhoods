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
with open('support/main_streets.geojson') as json_file:
    insert = 'INSERT INTO project.geo_main_streets (code, name, status, sub_system, geometry) VALUES ('
    data = json.load(json_file)
    for f in data['features']:
        if f['geometry']['type'] == 'LineString':
            code = f['properties']['CODVIA']
            name =  f['properties']['NMVIA']
            status=  f['properties']['STATUS']
            sub_system = f['properties']['SIST_VIARI']
            geometry = json.dumps(f['geometry'])
            
            if code == None:
                code = 'NULL'
            else:
                code = '\'' + str(db.escape_string(code), 'utf-8') + '\''
            
            if name == None:
                name = 'NULL'
            else:
                name = '\'' + str(db.escape_string(name), 'utf-8') + '\''

            #print(db.escape_string(name))
            sql_insert = insert + code + ', ' + name + ', \'' + str(db.escape_string(status), 'utf-8') + '\', \'' + str(db.escape_string(sub_system), 'utf-8') + '\', ST_SwapXY(ST_GeomFromGeoJSON(\'' + geometry + '\')));'
            cur.execute(sql_insert)
            print(x)
        x = x + 1
db.commit()
db.close()