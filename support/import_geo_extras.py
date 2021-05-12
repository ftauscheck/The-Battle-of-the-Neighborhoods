def geo2mysql(option, geojson_file):
    x = 0
    with open(geojson_file, encoding='utf-8') as json_file:
        insert = 'INSERT INTO project.geo_extras ( type, name, smm_code, geometry) VALUES ('
        data = json.load(json_file)
        for f in data['features']:
            type = 'NULL' if dot_get(f, 'properties.TIPO') == None else '\'' + str(db.escape_string(dot_get(f, 'properties.TIPO')), 'utf-8') + '\''
            name = 'NULL' if dot_get(f, 'properties.NOME') == None else '\'' + str(db.escape_string(dot_get(f, 'properties.NOME')), 'utf-8') + '\''
            smm_code = 'NULL' if dot_get(f, 'properties.CODIGO_SMM') == None else '\'' + str(db.escape_string(dot_get(f, 'properties.CODIGO_SMM')), 'utf-8') + '\''
            geometry = json.dumps(f['geometry'])
            sql_insert = insert + type + ', ' + name + ', ' + smm_code + ', ST_GeomFromGeoJSON(\'' + geometry + '\'));'
            #print(sql_insert)
            cur.execute(sql_insert)
            x = x + 1
    db.commit()
    print('{} - INSERT {}'.format(option, x))

def dot_get(dictionary, dot_path, default=None):
    from functools import reduce
    path = dot_path.split('.')
    try:
        return reduce(dict.__getitem__, path, dictionary)
    except KeyError:
        return default
    except TypeError:
        return default

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
cur.execute("TRUNCATE project.geo_extras;")

geo2mysql('BoardWalk', 'support/GeoJSON/Curitiba_boardwalk.geojson')
geo2mysql('Parks', 'support/GeoJSON/Curitiba_parks.geojson')
geo2mysql('Public Square', 'support/GeoJSON/Curitiba_public_square.geojson')

db.close()
