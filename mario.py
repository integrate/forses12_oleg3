import wrap
from wrap import sprite

def add_mario(x,y):
    id=sprite.add('mario-1-big',x,y,'stand')
    return id

def move_mario_y(id):
    x,y=sprite.get_pos(id)
    while y<=580:
        sprite.move(id,0,9)
        x,y=sprite.get_pos(id)