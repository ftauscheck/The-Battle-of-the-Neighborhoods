import json
import psycopg2
import configparser
import unidecode

config = configparser.ConfigParser()
config.read('config.ini')
database = config['postgis']

conn_string = "host='"+ database['host'] +"' user='" + database['user'] + "' password='"+ database['passwd']+"'"
conn=psycopg2.connect(conn_string)

cur = conn.cursor()
cur.execute("TRUNCATE project.geo_neighbourhood;")
x = 0
with open('support/GeoJSON/Curitiba_neighbourhood.geojson', encoding='utf-8') as json_file:
    insert = 'INSERT INTO project.geo_neighbourhood (id, type, neighbourhood, norm_neighbourhood, area, sectional_id, sectional_name, geometry) VALUES ('
    data = json.load(json_file)
    for f in data['features']:
        id = f['properties']['CODIGO']
        type =  f['properties']['TIPO']
        neighbourhood=  f['properties']['NOME']
        norm_neighbourhood=  unidecode.unidecode(neighbourhood).upper()
        area = f['properties']['SHAPE_AREA']
        sectional_id = f['properties']['CD_REGIONA']
        sectional_name = f['properties']['NM_REGIONA']
        geometry = json.dumps(f['geometry'])
        sql_insert = insert + str(id) + ', \''+ type + '\', \'' + neighbourhood + '\', \'' + norm_neighbourhood + '\', ' + str(area) + ', ' + str(sectional_id)+ ', \'' + sectional_name + '\', ST_GeomFromGeoJSON(\'' + geometry + '\'));'
        cur.execute(sql_insert)
        x = x + 1
conn.commit()
print('Neighbourhood: INSERT {}'.format(x))

x = 0
with open('support/GeoJSON/Curitiba_neighbourhood_simple.geojson', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for f in data['features']:
        id = f['properties']['CODIGO']
        geometry = json.dumps(f['geometry'])
        sql_update = 'UPDATE project.geo_neighbourhood SET geometry_simple = ST_GeomFromGeoJSON(\'' + geometry + '\') WHERE id = ' + str(id) + ';'
        cur.execute(sql_update)
        x = x + 1
conn.commit()
print('Neighbourhood: UPDATE {}'.format(x))
conn.close()
