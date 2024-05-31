import sqlite3

class ConexionDB:
    def __init__(self):
        #create new db or connect to a db
        self.base_datos = "database/peliculas.db"
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
    
    #close connection to db
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()