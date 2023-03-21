from tkinter import messagebox
import sqlite3

def startConnection():
    try:
        myConnection = sqlite3.connect("db_people")
        myCursor = myConnection.cursor()

        myCursor.execute("""CREATE TABLE PEOPLE 
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        FIRST_NAME VARCHAR(50),
                        LAST_NAME VARCHAR(50),
                        PASSWORD VARCHAR(30),
                        ADDRESS VARCHAR(30),
                        COMMENTS VARCHAR(100)
                        )""")
        return messagebox.showinfo("Éxito", "DB creada")
    except:
        return messagebox.showwarning("Atención", "La db ya existe")

def closeConnection():
    myConnection = sqlite3.connect("db_people")
    return myConnection.close()

def insertData(name:str, last_name:str, password:str, address:str, comments:str):
    myConnection = sqlite3.connect("db_people")
    myCursor = myConnection.cursor()
    
    if name != "" and last_name != "" and password != "" and address != "" and comments != "":
        myCursor.execute(f"""INSERT INTO PEOPLE (FIRST_NAME, LAST_NAME, PASSWORD, ADDRESS, COMMENTS)
                VALUES ('{name}','{last_name}','{password}','{address}', '{comments}')""")        
        myConnection.commit()
        return messagebox.showinfo("Éxito", f"Se han creado los datos de la persona {name}")
    else:
        return messagebox.showerror("Error", "Rellenar todos los campos")
            
def showData():
    myConnection = sqlite3.connect("db_people")
    myCursor = myConnection.cursor()
    
    myCursor.execute("SELECT * FROM PEOPLE")
    datos = (myCursor.fetchall())
    myConnection.commit()
    
    return datos

def searchData(id:int):
    myConnection = sqlite3.connect("db_people")
    myCursor = myConnection.cursor()
    
    datos = myCursor.execute(f"SELECT * FROM PEOPLE WHERE ID='{id}'")
    myConnection.commit()
    for person in datos:    
        return person 

def updateData(id:int, name:str, last_name:str, password:str, address:str, comments:str):
    myConnection = sqlite3.connect("db_people")
    myCursor = myConnection.cursor()
    
    if id == "" and name == "" and last_name == "" and password == "" and address == "" and comments == "":
        return messagebox.showerror("Error", "Rellenar todos los campos")
    
    myCursor.execute(f"""UPDATE PEOPLE SET FIRST_NAME='{name}', LAST_NAME='{last_name}', PASSWORD='{password}', ADDRESS='{address}', COMMENTS = '{comments}'  WHERE ID='{id}' """)
    myConnection.commit()
    
    if myCursor.rowcount > 0:
        return messagebox.showinfo("Éxito", "Se han actualizado los datos")
    else:
        return messagebox.showerror("Error", "Datos a actualizar no encontrados")

def deleteData(id:int):
    myConnection = sqlite3.connect("db_people")
    myCursor = myConnection.cursor()
    
    myCursor.execute(f"DELETE FROM PEOPLE WHERE id='{id}'")
    myConnection.commit()
    
    if myCursor.rowcount > 0:
        return messagebox.showinfo("Éxito", "Se han eliminado los datos")
    else:
        return messagebox.showerror("Error", "Datos no encontrados")
    


# insertData('José', 'Quispe', '123', 'Mi casa', 'Hola')
# updateData(14,'José Leandro', 'Quispe Reyes', '434', 'Mi casa', 'Hola')
# deleteData(16)
# showData()
# print(searchData(16))
# startConnection()
# closeConnection()



# Insertar datos
# myCursor.execute("""INSERT INTO PEOPLE (FIRST_NAME, LAST_NAME, PASSWORD, ADDRESS, COMMENTS)
#                 VALUES ('José','Quispe','123','Mi casa', 'Hola mundo')""")

# Eliminar datos
# myCursor.execute("""DELETE FROM PEOPLE WHERE ID=2""")

# Actualizar datos
# myCursor.execute("""UPDATE PEOPLE SET FIRST_NAME=FIRST_NAME, LAST_NAME='Quispe Reyes' WHERE ID=1 """)

# Leer datos
# myCursor.execute("SELECT * FROM PEOPLE")
# print(myCursor.fetchall())