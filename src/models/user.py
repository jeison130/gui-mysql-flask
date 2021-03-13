from src.connection_bd.bd import mysql
from flask import request, redirect, flash
from src.dto.user import UserDTO

class UsersModel():
    def lists(self):
        cursor = mysql.get_db().cursor()
        #cursor = mysql.get_db().cursor()
        cursor.execute('select * from user') 

        fields_name = [field[0] for field in cursor.description]
        data = cursor.fetchall()

        response = []

        for index, d in enumerate(data):
            response.append({})
            for index_field, field in enumerate(fields_name):
                response[index][fields_name[index_field]] = d[index_field]

        cursor.close()
        print(data)
        return response

    def create(self, user: UserDTO):
        cursor = mysql.get_db().cursor()
        #cursor = mysql.cursor()
        cursor.execute("""insert into user 
            (name,lastname,phone,email,password) 
            values (%s,%s,%s,%s,%s)""", (user.name,user.lastname,user.phone,user.email,user.password,))

        mysql.get_db().commit()
        cursor.close()

    def update(name, lastname,phone,email,password,id):
        cursor = mysql.get_db().cursor()
        #cursor = mysql.cursor()
        cursor.execute('update register set name = ?,lastname = ?,phone = ?,email = ?,password = ? WHERE id = ?', (name, lastname,phone,email,password,id,))
        mysql.get_db().commit()
        cursor.close()
        print(data)
            
    def delete(id):
        cursor = mysql.get_db().cursor()
        #cursor = mysql.cursor()
        cursor.execute('delete from register where id = %s', (id,))
        mysql.get_db().commit()
        cursor.close()