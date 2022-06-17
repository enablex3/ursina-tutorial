from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

stone_floor = "textures/ground/stone_floor/tiled_basecolor.jpg"

MAXIMUM_GRAB_DISTANCE = 3

def update():
    global grab_entity

    if cube.hovered:

        if distance(player, cube) <= MAXIMUM_GRAB_DISTANCE:
            grab_entity = True
        else:
            grab_entity = False

    else:
        grab_entity = False

    if grab_entity:
        if mouse.left:
            cube.world_position += player.cursor.world_position
grab_entity = False

window.show_ursina_splash = True

app = Ursina()

ground = Entity(model="plane", texture=stone_floor, collider="mesh", scale=(100, 1, 100))
cube = Entity(model="cube", color=color.olive, collider="mesh", scale=(1, 1, 1), position=(0, 0.5, 0))

Sky()

player = FirstPersonController()

app.run()
