from tkinter import *
from connection import *
from functions import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("CRUD")

# Menu Bar
menu = Menu(root)
root.config(menu=menu, width=300, height=300)

menuBBDD = Menu(menu, tearoff=0)
menuBBDD.add_command(label="Conectar", command=lambda:startConnection())
menuBBDD.add_command(label="Ver Datos", command=lambda:showAllData())
menuBBDD.add_separator()
menuBBDD.add_command(label="Salir", command=lambda:exitApp(root))
menu.add_cascade(label="BBDD", menu=menuBBDD)

menuDelete = Menu(menu, tearoff=0)
menuDelete.add_command(label="Limpiar Campos", command=lambda:deleteInputsText())
menu.add_cascade(label="LIMPIAR", menu=menuDelete)

menuCRUD = Menu(menu, tearoff=0)
menuCRUD.add_command(label="Crear", command=lambda:createPerson())
menuCRUD.add_command(label="Leer", command=lambda:readPerson(Id.get()))
menuCRUD.add_command(label="Actualizar", command=lambda:updatePerson())
menuCRUD.add_command(label="Borrar", command=lambda:deletePerson())
menu.add_cascade(label="CRUD", menu=menuCRUD)

menuHelp = Menu(menu, tearoff=0)
menuHelp.add_command(label="Licencia", command=lambda:helpFunction(False))
menuHelp.add_command(label="Acerca de", command=lambda:helpFunction(True))
menu.add_cascade(label="AYUDA", menu=menuHelp)



# Content
framePeople = Frame(root)
framePeople.pack(pady=10, padx=25)


Label(framePeople, text="ID:").grid(row=0, column=1, pady=8, padx=8)
Label(framePeople, text="Nombre:").grid(row=1, column=1, pady=8, padx=8)
Label(framePeople, text="Apellido:").grid(row=2, column=1, pady=8, padx=8)
Label(framePeople, text="Password:").grid(row=3, column=1, pady=8, padx=8)
Label(framePeople, text="Dirección:").grid(row=4, column=1, pady=8, padx=8)
Label(framePeople, text="Comentarios:").grid(row=5, column=1, pady=8, padx=8)


Id = StringVar() 
Name = StringVar() 
LastName = StringVar() 
Password = StringVar() 
Address = StringVar() 


inputId = Entry(framePeople, textvariable=Id).grid(row=0, column=2)
inputName = Entry(framePeople, textvariable=Name).grid(row=1, column=2)
inputLastName = Entry(framePeople, textvariable=LastName).grid(row=2, column=2)
inputPassword = Entry(framePeople, textvariable=Password, show="*").grid(row=3, column=2)
inputAddress = Entry(framePeople, textvariable=Address).grid(row=4, column=2)
commentsText = Text(framePeople, width=20, height=4)
commentsText.grid(row=5, column=2, pady=8)
scrollComments = Scrollbar(framePeople, command=commentsText.yview)
scrollComments.grid(row=5, column=3, pady=8, sticky="nsew")
commentsText.config(yscrollcommand=scrollComments.set)


Button(framePeople, text="Crear", command=lambda:createPerson()).grid(row=6, column=0)
Button(framePeople, text="Leer", command=lambda:readPerson(Id.get())).grid(row=6, column=1)
Button(framePeople, text="Actualizar", command=lambda:updatePerson()).grid(row=6, column=2)
Button(framePeople, text="Borrar", command=lambda:deletePerson()).grid(row=6, column=3)


# Functions
def updateCommentsWidget(data):
	commentsText.delete(1.0, END)
	commentsText.insert(END,data)

def deleteInputsText():
	Id.set(""),Name.set(""), LastName.set(""), Password.set(""), Address.set(""), updateCommentsWidget("")

def readPerson(id:int):
	try:
		datos = searchData(id)
		Name.set(datos[1]), LastName.set(datos[2]), Password.set(datos[3]), Address.set(datos[4]), updateCommentsWidget(datos[5])
	except:
		messagebox.showerror("Error", "Datos no encontrados")

def createPerson():
	insertData(Name.get(), LastName.get(), Password.get(), Address.get(), commentsText.get(1.0, END))

def updatePerson():
	updateData(Id.get() ,Name.get(), LastName.get(), Password.get(), Address.get(), commentsText.get(1.0, END))

def deletePerson():	
	deleteData(Id.get())

root.mainloop()