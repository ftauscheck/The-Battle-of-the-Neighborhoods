import json
import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
database = config['postgis']

conn_string = "host='"+ database['host'] +"' user='" + database['user'] + "' password='"+ database['passwd']+"'"
conn=psycopg2.connect(conn_string)

cur = conn.cursor()
x = 1
with open('support/GeoJSON/Curitiba_main_streets.geojson', encoding='utf-8') as json_file:
    insert = 'INSERT INTO project.geo_main_streets (code, name, status, sub_system, geometry) VALUES ('
    data = json.load(json_file)
    for f in data['features']:
        if f['geometry']['type'] == 'LineString':
            code = 'NULL' if f['properties']['CODVIA'] == None else f['properties']['CODVIA']
            name =  'NULL' if f['properties']['NMVIA'] == None else f['properties']['NMVIA']
            status=  f['properties']['STATUS']
            sub_system = f['properties']['SIST_VIARI']
            geometry = json.dumps(f['geometry'])
            # sql_insert = insert + code + ', ' + name + ', \'' + str(conn.escape_string(status), 'utf-8') + '\', \'' + str(conn.escape_string(sub_system), 'utf-8') + '\', ST_SwapXY(ST_GeomFromGeoJSON(\'' + geometry + '\')));'
            sql_insert = 'INSERT INTO project.geo_main_streets (code, name, status, sub_system, geometry) VALUES ( %s, %s, %s, %s, ST_GeomFromGeoJSON(%s));' 
            cur.execute(sql_insert, (code, name, status, sub_system, geometry))
        x = x + 1

print('Main Streets - INSERT {}'.format(x))
conn.commit()
conn.close()