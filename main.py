from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

MAZE_SCALE = 5
PLAYER_STARTING_POSITION = (-28.889, 0, 16.485)

def update():
    if player.y < 0:
        player.position = PLAYER_STARTING_POSITION

def input(key):
    if key == "escape":
        quit()

app = Ursina()

maze = Entity(model="models/maze", texture="brick", scale=MAZE_SCALE, collider="mesh")

player = FirstPersonController(position=PLAYER_STARTING_POSITION)
app.run()
