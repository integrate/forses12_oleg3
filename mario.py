import wrap
from wrap import sprite

def add_mario(x,y,speed):
    id=sprite.add('mario-1-big',x,y,'stand')
    f={'id':id,'speed':speed}
    return f

def move_mario_y(mario):

    x,y=sprite.get_pos(mario['id'])
    if y<=580:
        sprite.move(mario['id'],0,mario['speed'])
        mario['speed']+=1
        x, y = sprite.get_pos(mario['id'])
    if y >= 580:
        sprite.move_to(mario['id'], x, 580)