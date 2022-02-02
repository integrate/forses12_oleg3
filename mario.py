import wrap
from wrap import sprite


def add_mario(x, y, speed):
    id = sprite.add('mario-1-big', x, y, 'stand')
    f = {'id': id, 'speed': speed}
    return f


def move_mario_y(mario, ground):
    y = sprite.get_bottom(mario['id'])
    if y <= ground:
        sprite.move(mario['id'], 0, mario['speed'])
        mario['speed'] += 1
        y = sprite.get_bottom(mario['id'])
    if y >= ground:
        sprite.move_bottom_to(mario['id'], ground)


def prizok(mario, ground):
    y = sprite.get_bottom(mario['id'])
    ground = sprite.get_top(ground)
    if y == ground:
        mario['speed'] = -10
    # move_mario_y(mario,ground)


def go_x(mario, side):
    if side == 'right':
        sprite.move(mario['id'], 3, 0)
    elif side == 'left':
        sprite.move(mario['id'], -3, 0)
