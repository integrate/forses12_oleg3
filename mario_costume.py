import wrap
from wrap import sprite



def set_costum_jump(mario):
    sprite.set_costume(mario['id'], 'jump')


def set_costum_stand(mario):
    sprite.set_costume(mario['id'], 'stand')

def look_right(mario):
    sprite.set_reverse_x(mario['id'],False)

def look_left(mario):
    sprite.set_reverse_x(mario['id'],True)

def animation_go(mario):
    c=sprite.get_costume(mario['id'])
    if c=='stand' or c=='walk3':
        y = sprite.get_bottom(mario['id'])
        sprite.set_costume(mario['id'], 'walk1')
        sprite.move_bottom_to(mario['id'], y)
    elif c=='walk1':
        y=sprite.get_bottom(mario['id'])
        sprite.set_costume(mario['id'], 'walk2')
        sprite.move_bottom_to(mario['id'], y)

    elif c=='walk2':
        y = sprite.get_bottom(mario['id'])
        sprite.set_costume(mario['id'], 'walk3')
        sprite.move_bottom_to(mario['id'], y)


