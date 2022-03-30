import wrap
from wrap import sprite
import costume_helper

def set_costum_jump(mario):
    costume_helper.change_costume(mario['id'], 'dragon_throw1')


def set_costum_stand(mario):
    costume_helper.change_costume(mario['id'], 'dragon_stand1')


def look_right(mario):
    sprite.set_reverse_x(mario['id'], True)


def look_left(mario):
    sprite.set_reverse_x(mario['id'], False)


def animation_go(mario):
    c = sprite.get_costume(mario['id'])
    if c == 'dragon_stand2':
        costume_helper.change_costume(mario['id'], 'dragon_stand1')
    elif c == 'dragon_stand1':
        costume_helper.change_costume(mario['id'], 'dragon_stand2')
