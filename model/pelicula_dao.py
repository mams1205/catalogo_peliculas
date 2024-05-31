from model.conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()
    
    #sql code to create the db
    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )'''
    
    #execute sql
    try: 
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Crear Registro"
        mensaje = "Se creo la tabla en la base de datos"
        messagebox.showinfo(titulo, mensaje)
        
    except:
        titulo = "Crear Registro"
        mensaje = "La tabla ya esta creada"
        messagebox.showwarning(titulo, mensaje)
    
    
def borrar_tabla():
    conexion = ConexionDB()
    
    sql = 'DROP TABLE peliculas'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Borrar Registro"
        mensaje = "Se borro la tabla en la base de datos con éxito"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Borrar Registro"
        mensaje = "La tabla no existe, no hay tabla para borrar"
        messagebox.showerror(titulo, mensaje)
        
class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
    
    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'
    
#function for insert values in the fields of the data base
def guardar(pelicula):
    conexion = ConexionDB()
    sql = f""" INSERT INTO peliculas (nombre, duracion, genero)
    VALUES('{pelicula.nombre}', '{pelicula.duracion}','{pelicula.genero}' )"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Conexión al Registro"
        mensaje = "La tabla no esta creada en la base de datos"
        messagebox.showerror(titulo, mensaje)

#funcion para mostrar todos los registros en la pantalla
def listar():
    conexion = ConexionDB()
    
    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'
    
    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
        
    except:
        titulo = "Conexion al registro"
        mensaje = "Crea la tabla en la Base de datos"
        messagebox.showwarning(titulo, mensaje)
    return lista_peliculas

#funcion para el boton editar
def editar(pelicula, id_pelicula):
    conexion = ConexionDB()
    sql = f"""UPDATE peliculas
    SET nombre = '{pelicula.nombre}', 
        duracion = '{pelicula.duracion}',
        genero = '{pelicula.genero}'
        WHERE id_pelicula = {id_pelicula} """
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Edicion de datos"
        mensaje = "No se ha podido editar este registro"
        messagebox.showerror(titulo, mensaje)
#funcion para el boton eliminar
def eliminar(id_pelicula):
    conexion = ConexionDB()
    sql = f"""DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Eliminar de registro"
        mensaje = "No se ha podido eliminar el registro"
        messagebox.showerror(titulo, mensaje)
    

        
    
    
        