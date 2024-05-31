import tkinter as tk
from tkinter import ttk #import to create a table
from tkinter import messagebox
from model.pelicula_dao import crear_tabla, borrar_tabla
from model.pelicula_dao import Pelicula, guardar, listar, editar, eliminar

#design the menu bar
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu,
                width = 300,
                height = 300)
    #first object of the menu INICIO
    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = "Inicio", menu = menu_inicio)
   
    
    #add commands to inicio
    menu_inicio.add_command(label = "Crear un registro en base de datos", command = crear_tabla )
    menu_inicio.add_command(label = "Eliminar un registro en base de datos", command = borrar_tabla)
    menu_inicio.add_command(label = "Salir", command = root.destroy )
    
     #other object to the barra menu
    menu_consultas = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = "Consultas", menu = menu_consultas)
    
    #other object to the barra_menu
    menu_configuracion = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = "Configuración", menu = menu_configuracion)
    
    #other object to the barra_menu
    menu_ayuda = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = "Ayuda", menu = menu_ayuda)
    
#create a class 
#constructor -> esta es la pantalla que se va a ver
class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width = 480, height = 320)
        self.root = root
        self.pack()
        # self.config(bg = "green")
        self.id_pelicula = None
        
        self.campos_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()
    #aqui se añade una etiqueta a la pantalla
    #object of the frame class -> cuadro   
    def campos_pelicula(self):
        #Labels for each field
        self.label_nombre = tk.Label(self, text = "Nombre: ")
        self.label_duracion = tk.Label(self, text = "Duración: ")
        self.label_genero = tk.Label(self, text = "Género: ")
        
        #configure the labels 
        self.label_nombre.config(font = ("Arial", 12, "bold"))
        self.label_duracion.config(font = ("Arial", 12, "bold"))
        self.label_genero.config(font = ("Arial", 12, "bold"))
        
        #where the labels will be located? using grid -> rows and columns
        self.label_nombre.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.label_duracion.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.label_genero.grid(row = 2, column = 0, padx = 10, pady = 10)
        
        #Entrys for each field
        #Entry nombre
        self.mi_nombre = tk.StringVar() #objeto de texto
        self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
        self.entry_nombre.config(width = 50, font = ("Arial", 12,)) #configure entry field
        self.entry_nombre.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2)  #position of each field
        
        #entry duracion
        self.mi_duracion = tk.StringVar() #objeto de texto
        self.entry_duracion = tk.Entry(self, textvariable = self.mi_duracion)
        self.entry_duracion.config(width = 50, font = ("Arial", 12))
        self.entry_duracion.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)
        
        #entry genero
        self.mi_genero = tk.StringVar() #objeto de texto
        self.entry_genero = tk.Entry(self, textvariable = self.mi_genero)
        self.entry_genero.config(width = 50,  font = ("Arial", 12))
        self.entry_genero.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan = 2)
        
        #Buttons
        #boton para nuevo registro
        self.boton_nuevo = tk.Button(self, text = "Nuevo", command = self.habilitar_campos)
        self.boton_nuevo.config(width = 20, font = ("Arial", 12, "bold"), 
                                bg = "forest green", fg = "white", #background and font color
                                cursor = "hand2", #cursor shape 
                                activebackground = "yellow green") 
        self.boton_nuevo.grid(row = 3, column = 0, padx = 10, pady = 10)
        
        #boton para guardar
        self.boton_guardar = tk.Button(self, text = "Guardar", command = self.guardar_datos)
        self.boton_guardar.config(width = 20, font = ("Arial", 12, "bold"), 
                                bg = "RoyalBlue1", fg = "white", #background and font color
                                cursor = "hand2", #cursor shape 
                                activebackground = "DodgerBlue2") #color when you click the button
        self.boton_guardar.grid(row = 3, column = 1, padx = 10, pady = 10)
        
        #boton para cancelar
        self.boton_cancelar = tk.Button(self, text = "Cancelar", command = self.deshabilitar_campos)
        self.boton_cancelar.config(width = 20, font = ("Arial", 12, "bold"), 
                                bg = "red4", fg = "white", #background and font color
                                cursor = "hand2", #cursor shape 
                                activebackground = "red2") #color when you click the button
        self.boton_cancelar.grid(row = 3, column = 2, padx = 10, pady = 10)
        
    def habilitar_campos(self):
        #clean entry fields
        self.mi_nombre.set("")
        self.mi_duracion.set("")
        self.mi_genero.set("")
        
        #enable the entry fields
        self.entry_nombre.config(state = "normal")
        self.entry_duracion.config(state = "normal")
        self.entry_genero.config(state = "normal")
        
        #enable buttons
        self.boton_guardar.config(state = "normal")
        self.boton_cancelar.config(state = "normal")
        
    def deshabilitar_campos(self):
        #reset id 
        self.id_pelicula = None
        #clean entry fields
        self.mi_nombre.set("")
        self.mi_duracion.set("")
        self.mi_genero.set("")
        
        #disable the entry fields
        self.entry_nombre.config(state = "disabled")
        self.entry_duracion.config(state = "disabled")
        self.entry_genero.config(state = "disabled")
        
        #disable buttons
        self.boton_guardar.config(state = "disabled")
        self.boton_cancelar.config(state = "disabled")
        
    def guardar_datos(self):
        
        #give pelicula the data from the entry fields
        pelicula = Pelicula(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get(),
        )
        #save the data from the entry fields
         
        if self.id_pelicula == None:
            guardar(pelicula)
        
        else:
            editar(pelicula, self.id_pelicula)
            
        
        self.tabla_peliculas()
        
        #disable fields
        self.deshabilitar_campos()
        
        
    #create a table to see the entrys
    def tabla_peliculas(self):
        #recuperar lista de peliculas
        self.lista_peliculas = listar()
        #order from low to high ID
        self.lista_peliculas.reverse()
        
        #create table to show the entrys
        self.tabla = ttk.Treeview(self,
                                  column = ("Nombre", "Duración", "Género"))
        #add grid
        self.tabla.grid(row = 4, column = 0, columnspan = 4, sticky = "nse")
        
        #add scrollbar
        self.scroll = ttk.Scrollbar(self,
                                    orient = "vertical", 
                                    command = self.tabla.yview)
        self.scroll.grid(row = 4, column = 4, sticky = "nse")
        self.tabla.configure(yscrollcommand = self.scroll.set)
        
        #headings of the table
        self.tabla.heading("#0", text = "ID")
        self.tabla.heading("#1", text = "NOMBRE")
        self.tabla.heading("#2", text = "DURACIÓN")
        self.tabla.heading("#3", text = "GÉNERO")
        
        #iteration of lista de peliculas
        for p in self.lista_peliculas:
            self.tabla.insert("", 0, text = p[0], 
                          values = (p[1],p[2],p[3]))
        
        #boton editar
        self.boton_editar = tk.Button(self, text = "Editar", command = self.editar_datos)
        self.boton_editar.config(width = 20, font = ("Arial", 12, "bold"), 
                                bg = "forest green", fg = "white", #background and font color
                                cursor = "hand2", #cursor shape 
                                activebackground = "yellow green") 
        self.boton_editar.grid(row = 5, column = 0, padx = 10, pady = 10)
        
        #boton para eliminar
        self.boton_eliminar = tk.Button(self, text = "Eliminar", command = self.eliminar_datos)
        self.boton_eliminar.config(width = 20, font = ("Arial", 12, "bold"), 
                                bg = "red4", fg = "white", #background and font color
                                cursor = "hand2", #cursor shape 
                                activebackground = "red2") #color when you click the button
        self.boton_eliminar.grid(row = 5, column = 1, padx = 10, pady = 10)
    def editar_datos(self):
        try:
            #recuperar los datos de la tabla en los campos
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(
                self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(
                self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(
                self.tabla.selection())['values'][2]
            
            
            self.habilitar_campos()
            self.entry_nombre.insert(0,self.nombre_pelicula)
            self.entry_duracion.insert(0,self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)
        except:
            titulo = "Edicion de datos"
            mensaje = "No ha seleccionado ningun registro"
            messagebox.showerror(titulo, mensaje)
    def eliminar_datos(self):
        try:
            #recuperar los datos de la tabla en los campos
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_pelicula)
            
            self.tabla_peliculas()
            self.id_pelicula = None
            
        except:
            titulo = "Eliminar un registro"
            mensaje = "No se ha seleccionado ningun registro"
            messagebox.showerror(titulo, mensaje)
        