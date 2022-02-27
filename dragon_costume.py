import wrap
from wrap import sprite


def set_costum_jump(mario):
    sprite.set_costume(mario['id'], 'dragon_throw1')


def set_costum_stand(mario):
    sprite.set_costume(mario['id'], 'dragon_stand1')


def look_right(mario):
    sprite.set_reverse_x(mario['id'], True)


def look_left(mario):
    sprite.set_reverse_x(mario['id'], False)


def animation_go(mario):
    c = sprite.get_costume(mario['id'])
    if c == 'dragon_stand2':
        y = sprite.get_bottom(mario['id'])
        sprite.set_costume(mario['id'], 'dragon_stand1')
        sprite.move_bottom_to(mario['id'], y)
    elif c == 'dragon_stand1':
        y = sprite.get_bottom(mario['id'])
        sprite.set_costume(mario['id'], 'dragon_stand2')
        sprite.move_bottom_to(mario['id'], y)


