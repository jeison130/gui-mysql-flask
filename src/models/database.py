import src.config.globals as globals
class DatabaseModel():
    def list(self):
        cursor = globals.DB.cursor() 

        cursor.execute('show databases') 

        data = cursor.fetchall()
        
        cursor.close()

        return data
    
    def showTables(self, database):
        cursor = globals.DB.cursor() 

        cursor.execute('use ' + database)
        cursor.execute('show tables')

        tables = cursor.fetchall()
        
        cursor.close()

        return tables

    def showFields(self, database, table):
        cursor = globals.DB.cursor() 

        cursor.execute('use ' + database)
        cursor.execute('describe ' + table)
        
        fields = cursor.fetchall()
        
        cursor.close()

        return fields

    def showData(self, database, table):
        cursor = globals.DB.cursor() 

        cursor.execute('use ' + database)
        cursor.execute('select * from ' + table) 

        fields = cursor.description
        data = cursor.fetchall()
        
        cursor.close()

        return {
            'data': data, 
            'fields': fields
        }

    