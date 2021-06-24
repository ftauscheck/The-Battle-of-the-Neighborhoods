def geo2postgis(option, geojson_file):
    x = 0
    with open(geojson_file, encoding='utf-8') as json_file:
        insert = 'INSERT INTO project.geo_extras ( type, name, smm_code, geometry) VALUES ('
        data = json.load(json_file)
        for f in data['features']:
            type = 'NULL' if dot_get(f, 'properties.TIPO') == None else dot_get(f, 'properties.TIPO')
            name = 'NULL' if dot_get(f, 'properties.NOME') == None else dot_get(f, 'properties.NOME')
            smm_code = 'NULL' if dot_get(f, 'properties.CODIGO_SMM') == None else dot_get(f, 'properties.CODIGO_SMM')
            geometry = json.dumps(f['geometry'])
            sql_insert = 'INSERT INTO project.geo_extras ( type, name, smm_code, geometry) VALUES (%s, %s, %s, ST_GeomFromGeoJSON(%s));'
            cur.execute(sql_insert, (type, name, smm_code, geometry))
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
import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
database = config['postgis']

conn_string = "host='"+ database['host'] +"' user='" + database['user'] + "' password='"+ database['passwd']+"'"
db=psycopg2.connect(conn_string)

cur = db.cursor()

cur.execute("TRUNCATE project.geo_extras;")

geo2postgis('BoardWalk', 'support/GeoJSON/Curitiba_boardwalk.geojson')
geo2postgis('Parks', 'support/GeoJSON/Curitiba_parks.geojson')
geo2postgis('Public Square', 'support/GeoJSON/Curitiba_public_square.geojson')

db.close()