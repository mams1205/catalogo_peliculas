import tkinter as tk
from client.gui_app import Frame, barra_menu
def main():
    #create the object
    root = tk.Tk()
    #change the title of the window
    root.title("Catálogo de películas")
    #add the logo
    root.iconbitmap("img/logo.ico")
    #change the size of the window
    root.resizable(0,0)
    barra_menu(root)
    
    app = Frame(root = root)
    app.mainloop()
# Check if the script is being run directly by the Python interpreter
if __name__ =='__main__':
    # If the script is being run directly, call the 'main' function
    main()

