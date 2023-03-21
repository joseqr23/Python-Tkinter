from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from connection import showData

# Interface Menu Bar
def helpFunction(info: bool):
    if not info:
        return messagebox.showinfo("Licencia", "Sin licencia alguna")
    return messagebox.showinfo("Información", "Derechos reservados José")

def exitApp(root):
    myConnection = sqlite3.connect("db_people")

    if messagebox.askokcancel("Salir", "¿Deseas salir?"):
        myConnection.close()        
        root.destroy()
        return messagebox.showinfo("Éxito", "Se ha cerrado la conexión")

# Data
def showAllData():
    rootTwo = Tk()
    rootTwo.title("Datos de Personas")


    data = showData()
    treeview = ttk.Treeview(rootTwo, columns=("columna2", "columna3", "columna4", "columna5"))
    
    treeview.heading("columna2",text="Nombre")
    treeview.heading("columna3",text="Apellido")
    treeview.heading("columna4",text="Dirección")
    treeview.heading("columna5",text="Comentarios")

    for person in data:
        treeview.insert("", END, text=person[0], values=(person[1], person[2],person[4], person[5]))
    treeview.grid()
    rootTwo.mainloop() 