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
    sprite.set_costume(mario['id'],'walk1')
    sprite.set_costume(mario['id'],'walk2')
    sprite.set_costume(mario['id'],'walk3')

