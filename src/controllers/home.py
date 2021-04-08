from flask import render_template, redirect, url_for, request
from src import app
import src.config.globals as globals
from src.config.db import CONEXION_PATH, createConecction
import json
from src.models.database import DatabaseModel

databaseModel = DatabaseModel()

@app.route('/')
def index():
    if globals.DB == False:
        return redirect(url_for('access'))

    databases = databaseModel.list()

    return render_template('index.html', databases=databases)

@app.route('/database/<name>')
def listTables(name):
    databases = databaseModel.list()
    tables = databaseModel.showTables(name)
    fields = []
    for index, table in enumerate(tables):
        fields.append(databaseModel.showFields(name, table[0]))

    return render_template('index.html', 
        database=name,
        databases=databases, 
        tables=tables,
        fields=fields)

@app.route('/database/<name>/<table>')
def detailTable(name, table):
    response = databaseModel.showData(name, table)
    data = response['data']
    fields = response['fields']

    return render_template('datos_tabla.html', 
        database=name, 
        table=table,
        data=data,
        fields=fields,)

@app.route('/access', methods=['GET', 'POST'])
def access():
    print(globals.DB)
    if globals.DB != False:
        return redirect(url_for('index'))

    if request.method == 'GET':
        return render_template('access.html')

    datos = {
        "user": request.form.get('user'),
        "password": request.form.get('password'),
        "host": request.form.get('host'),
        "port": int(request.form.get('port')),
    }

    conexion = open(CONEXION_PATH, 'w')

    conexion.write(json.dumps(datos))

    conexion.close()
    createConecction()
    return redirect(url_for('index'))



    