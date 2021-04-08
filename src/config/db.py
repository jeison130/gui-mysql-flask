import src.config.globals as globals
from os import path
import mariadb
import json

CONEXION_PATH = path.abspath('src/config/conexion.json')

def createConecction():
    if path.exists(CONEXION_PATH):
        print("existe")
        file_conexion = open(CONEXION_PATH, 'r')
    
        config = json.loads(file_conexion.read())

        globals.DB = mariadb.connect(**config)
        globals.DB.autocommit = True
    else:
        globals.DB = False

createConecction()