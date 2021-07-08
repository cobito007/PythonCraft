from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
from Scripts.Tree import wood
from Scripts.Tree import leaf
from Scripts.Mobs import Enderman
from random import uniform
from ursina.shaders import basic_lighting_shader
from Scripts.Mobs import Skeleton
from numpy import floor
from perlin_noise import PerlinNoise

build_mode = True
block_pick = 1
grass = 'Scripts/Texture/Grass.png'
brick = 'Scripts/Texture/brick.png'
amp = 5
freq = 24

app = Ursina()
prevTime = time.time()
Player = FirstPersonController(position = (0, 15, 5))
cube = Entity(model='cube',texture=grass)
text1 = Text(text='Made with ursina engine', scale = 5, position=(-0.7,0.2))
destroy(text1, delay=5)
###Function for placing blocks###
def Build():
    cube.texture = grass
    cube.collider = 'cube'
    duplicate(cube)
###Update function for setting textures and
def update():
    global block_pick
    global player_timeout
    global health
    global x_
    global z_
    if held_keys['1']:
        block_pick = 1
        print(block_pick)
    if held_keys['2']:
        block_pick = 2
        print(block_pick)
    if held_keys['3']:
        block_pick = 3
        print(block_pick)
    skele.lookAt(Player)


    enderman.x += uniform(1, 5)
    enderman.x -= uniform(1, 5)
    enderman.z += uniform(1, 5)
    enderman.z -= uniform(1, 5)

def input(key):
    if key == 'escape':
        quit()

    global build_mode
    if build_mode == True:
        if key == 'right mouse down':
            Build()

class Blocks(Button):
    global Ground_textures
    def __init__(self, position = (0,0,0), texture = grass):
        super().__init__(
            parent = scene,
            position = position,
            origin_y = -5,
            model = 'cube',
            texture = texture,
            color = color.white
            )
class sky(Entity):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            model = 'sphere',
            color = color.cyan,
            double_sided = True,
            scale = 1000
            )

class tree(Entity):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            leaves = leaf(position = position),
            Wood = wood(position = position)
            )

for e in scene.entities:
    e.shader = basic_lighting_shader

terrain = Entity(model=None, collider=None)
terrain_width = 8
noise = PerlinNoise(octaves=4, seed=randint(0, 10000000))
for i in range(terrain_width * terrain_width):
    block = Blocks(position=(0, 0, 0))
    block.x = floor(i / terrain_width)
    block.z = floor(i % terrain_width)
    block.y = floor((noise([block.x / freq, block.z / freq])) * amp)
    block.parent = terrain
terrain.combine()
terrain.collider = 'mesh'
terrain.texture = grass

block = Blocks(position=(0,0,0))
World = sky()
tree1 = tree(position = (randint(0,20),2,randint(0,20)))
enderman = Enderman(position = (10,2,10))
skele = Skeleton(position = (0,2,5))
app.run()