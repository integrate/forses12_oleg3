import wrap
from wrap import sprite

def add_mario(x,y,speed):
    id=sprite.add('mario-1-big',x,y,'stand')
    f={'id':id,'speed':speed}
    return f

def move_mario_y(mario,ground):


    y=sprite.get_bottom(mario['id'])
    if y<=ground:
        sprite.move(mario['id'],0,mario['speed'])
        mario['speed']+=1
        y = sprite.get_bottom(mario['id'])
    if y >= ground:
        sprite.move_bottom_to(mario['id'], ground)

def prizok(mario,ground):
    mario['speed']=-10
    ground=sprite.get_top(ground)
    # move_mario_y(mario,ground)