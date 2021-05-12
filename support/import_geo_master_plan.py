import json
import MySQLdb
import configparser
# -proj from=EPSG:29192 wgs84

config = configparser.ConfigParser()
config.read('config.ini')
database = config['database']

db = MySQLdb.connect(host = database['host'],
                     port = int(database['port']),
                     user = database['user'],
                     passwd = database['passwd'])

cur = db.cursor()
cur.execute("TRUNCATE project.geo_master_plan;")
x = 0
y = 0
with open('support/GeoJSON/Curitiba_master_plan.geojson', encoding='utf-8') as json_file:
    insert = 'INSERT INTO project.geo_master_plan (nm_groups, cd_zone, nm_zone, sg_zone, area, lenght, geometry) VALUES ('
    data = json.load(json_file)
    for f in data['features']:
        if f['geometry']['type'] == 'Polygon' or f['geometry']['type'] == 'MultiPolygon' :
            nm_groups = f['properties']['NM_GRUPO']
            cd_zone =  "" if f['properties']['CD_ZONA'] == None else f['properties']['CD_ZONA']
            nm_zone =  f['properties']['NM_ZONA']
            sg_zone = f['properties']['SG_ZONA']
            area =  f['properties']['AREA']
            lenght = f['properties']['LEN']
            geometry = json.dumps(f['geometry'])
            sql_insert = insert + ' \''+ nm_groups + '\', \'' + cd_zone + '\', \'' + nm_zone + '\', \'' + sg_zone + '\', ' + str(round(area,6)) + ',  ' + str(round(lenght,6)) + ', ST_GeomFromGeoJSON(\'' + geometry + '\'));'
            cur.execute(sql_insert)
            y = y + 1
        x = x + 1
db.commit()
print('Master Plan: INSERT {} of {}'.format(y, x))

# Update DB with simplified version of GeoJSON (to speedup visualization)
x = 0
y = 0
with open('support/GeoJSON/Curitiba_master_plan_simple.geojson', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for f in data['features']:
        if f['geometry']['type'] == 'Polygon' or f['geometry']['type'] == 'MultiPolygon' :
            cd_zone =  "" if f['properties']['CD_ZONA'] == None else f['properties']['CD_ZONA']
            area =  f['properties']['AREA']
            lenght = f['properties']['LEN']
            geometry = json.dumps(f['geometry'])
            sql_update = 'UPDATE project.geo_master_plan SET geometry_simple = ST_GeomFromGeoJSON(\'' + geometry + '\') WHERE cd_zone = \'' + cd_zone + '\' AND area = ' + str(round(area,6)) + ' AND lenght = ' + str(round(lenght,6)) + ';'
            cur.execute(sql_update)
            y = y + 1
        x = x + 1
db.commit()
print('Master Plan: UPDATE {} of {}'.format(y, x))

db.close()

