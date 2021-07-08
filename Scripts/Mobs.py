from ursina import *

health = 20

# This is the Mobs script where hostile mobs are coded in if your a moder and want to add a creature you can add it here or add it in the Mods script :)

###Enderman Class###
class Enderman(Button):
    def __init__(self, position = (0,0,0), rotation = (0,0,0)):
        super().__init__(
            parent = scene,
            color = color.black,
            model = 'cube',
            scale = (2,4,2),
            position = position,
            rotation = rotation
            )
###Skeleton Class###
class Skeleton(Button):
    def __init__(self, position = (0,0,0), rotation = (0,0,0)):
        super().__init__(
            parent = scene,
            model = 'cube',
            color = color.red,
            position = position,
            rotation = rotation,
        )
    def input(self, key, rotation = (0,0,0)):
        if self.hovered:
            if key == 'left mouse down':
                bullet = Entity(model = 'cube', color = color.black, scale = 0.5, rotation = self.rotation, position = self.position)
                bullet.animate_position(bullet.position + (bullet.forward * 150), duration=1)