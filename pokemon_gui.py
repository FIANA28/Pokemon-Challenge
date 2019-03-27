from guizero import App, TextBox, PushButton, Picture, Text, info
from pokebase import pokemon
from requests import get
from PIL import Image
from io import BytesIO

def fetch_pokemon():
    
    name = input_box.value
    try:
     poke = pokemon(name)
     pic = get(poke.sprites.front_default).content
     image = Image.open(BytesIO(pic))
     image.save("poke.gif")
     icon.value = "poke.gif"

    # get height and weight features
     txt_height.value = "Height: " + str(poke.height)
     txt_weight.value = "Weight: " + str(poke.weight)
     txt_message.value = " "

    except ValueError:
        info("Wrong name!", "Please try again")

app = App(title="Pokemon Fetcher", width=300, height=200)
input_box = TextBox(app, text="Name")
icon = Picture(app, image="poke.gif")
submit = PushButton(app, command=fetch_pokemon, text="Submit")

# display height and weight of poke
txt_height = Text(app, text="Height", size=8, color="blue")
txt_weight = Text(app, text="Weight", size=8, color="blue")
txt_message = Text(app, text=" ", size=12)


app.display()

                    
