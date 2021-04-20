import configparser
config = configparser.ConfigParser()
config.read('config.ini')
print(config.sections())
config['database']['host']

for key in config['database']:  
    print(key)