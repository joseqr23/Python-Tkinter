from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO

raiz = Tk()

raiz.title("PokeApi")
raiz.resizable(0,0)

# raiz.tk.call('wm', 'iconphoto', raiz._w, PhotoImage(file='./pokeball.ico'))

framePokemons = Frame(raiz)
framePokemons.pack()


pokeVar = StringVar()

title = Label(framePokemons, text="Pokemons")
title.config(font=("Verdana", 18))
title.grid(row=0, column=0, pady=8,columnspan=4)

title = Label(framePokemons, text="Escriba el nombre o número de órden del Pokemon")
title.config(font=("Verdana", 8))
title.grid(row=1, column=0,columnspan=4)


buscador = Entry(framePokemons, width=20, textvariable=pokeVar)
buscador.config(font=("Verdana",15))
buscador.grid(row=2, column=1)

def enviarTexto():
    try:
        url_pokemon= f"https://pokeapi.co/api/v2/pokemon/{pokeVar.get().lower()}"
        response = requests.get(url_pokemon)
        data = response.json()
        pokemon_photo = (data["sprites"]["other"]["official-artwork"]["front_default"])

        urlImage(pokemon_photo)
        pokeVar.set("")
        error.config(text="")
        
    except:
        imgPokemon.config(image="")
        error.config(text="No se encontro el pokemon")

button = Button(framePokemons, text="Enviar", command=lambda:enviarTexto())
button.grid(row=3, column=1, pady=8)


def sendPokemon(event):
    enviarTexto()
raiz.bind("<Return>", sendPokemon)

def urlImage(url):

    response = requests.get(url)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    imgPokemon.config(image=img)
    imgPokemon.image = img


imgPokemon = Label(framePokemons)
imgPokemon.grid(row=4, column=1)

error = Label(framePokemons)
error.grid(row=5, column=1)


raiz.mainloop()