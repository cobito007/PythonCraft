from ursina import *
from random import randint

health = 5
health_tree = 2

# this is the tree script where all the logic for the trees in the game is coded

class wood(Button):
    global leaves_size
    def __init__(self,position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            color = color.brown,
            highlight_color = color.lime,
            scale = (1,3,1),
            model = 'cube',
            )

    def input(self, key):
        global health
        if self.hovered:
            if key == 'left mouse down':
                health -= 1
                if health == 0:
                    destroy(self)
                    
class leaf(Button):
    def __init__(self, position = (0,10,0)):
        super().__init__(
            parent = scene,
            origin_y = -1,
            model = 'cube',
            color = color.green,
            position = position,
            scale = (2,2,2)
            )
    def input(self,key):
        global health_tree
        if self.hovered:
            if key == 'left mouse down':
                health_tree -= 1
                if health_tree == 0:
                    destroy(self)
        
        