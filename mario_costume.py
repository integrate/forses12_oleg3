import wrap
from wrap import sprite
import costume_helper

def set_costum_jump(mario):
    costume_helper.change_costume(mario['id'],'jump')


def set_costum_stand(mario):
    costume_helper.change_costume(mario['id'], 'stand')


def look_right(mario):
    sprite.set_reverse_x(mario['id'], False)


def look_left(mario):
    sprite.set_reverse_x(mario['id'], True)


def animation_go(mario):
    c = sprite.get_costume(mario['id'])
    if c == 'stand' or c == 'walk3':
        costume_helper.change_costume(mario['id'], 'walk1')

    elif c == 'walk1':
        costume_helper.change_costume(mario['id'], 'walk2')

    elif c == 'walk2':
        costume_helper.change_costume(mario['id'], 'walk3')