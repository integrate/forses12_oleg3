import wrap
from wrap import sprite


def add_mario(x, y, speed, path, costum, mod):
    id = sprite.add(path, x, y, costum)
    f = {'id': id, 'speed': speed, 'mod_costum': mod}
    return f


def move_mario_y(mario, ground):
    y = sprite.get_bottom(mario['id'])
    if y <= ground:
        sprite.move(mario['id'], 0, mario['speed'])
        mario['speed'] += 1
        y = sprite.get_bottom(mario['id'])
    if y >= ground:
        sprite.move_bottom_to(mario['id'], ground)
        mario['mod_costum'].set_costum_stand(mario)


def prizok(mario, ground):
    y = sprite.get_bottom(mario['id'])
    ground = sprite.get_top(ground)
    if y == ground:
        mario['speed'] = -10
        mario['mod_costum'].set_costum_jump(mario)

    # move_mario_y(mario,ground)


def go_x(mario, side):
    if side == 'right':
        sprite.move(mario['id'], 3, 0)
    elif side == 'left':
        sprite.move(mario['id'], -3, 0)
