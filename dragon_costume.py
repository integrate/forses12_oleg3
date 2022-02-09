import wrap
from wrap import sprite


def set_costum_jump(mario):
    sprite.set_costume(mario['id'], 'dragon_throw1')


def set_costum_stand(mario):
    sprite.set_costume(mario['id'], 'dragon_stand1')

def look_right(mario):
    sprite.set_reverse_x(mario['id'],True)

def look_left(mario):
    sprite.set_reverse_x(mario['id'],False)

def animation_go(mario):
    sprite.set_costume(mario['id'],'dragon_stand1')
    sprite.set_costume(mario['id'],'dragon_stand2')




