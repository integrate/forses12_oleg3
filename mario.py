from wrap import sprite
import costume_helper


def add_mario(x, y, speed, path, costum, mod, grounds):
    id = sprite.add(path, x, y, costum)
    f = {'id': id, 'speed': speed, 'mod_costum': mod, 'grounds': grounds}
    mario_1_ground = found_ground(f, grounds)
    f['help'] = mario_1_ground
    f['text'] = None
    return f


def move_mario_y(mario):
    y = sprite.get_bottom(mario['id'])
    sprite.move(mario['id'], 0, mario['speed'])
    if y < mario['help']:
        mario['speed'] += 1
        y = sprite.get_bottom(mario['id'])
    if y > mario['help']:
        sprite.move_bottom_to(mario['id'], mario['help'])
        mario['mod_costum'].set_costum_stand(mario)
        mario['speed'] = 0
    mario['help'] = found_ground(mario, mario['grounds'])

def move_mario_y_this_dead(mario,teleport):
    if sprite.get_bottom(mario['id'])<600:
        move_mario_y(mario)
        return 'move_y'
    elif sprite.get_bottom(mario['id'])>600 and teleport == True:
        sprite.move_to(mario['id'], 800, 100)
        return 'teleport'
    elif sprite.get_bottom(mario['id'])>600 and teleport == False:
        sprite.move(mario["id"], 0, 1)
        return 'dead'






#     if teleport == True :
#         sprite.move_to()


def prizok(mario):
    y = sprite.get_bottom(mario['id'])

    if y == mario['help']:
        mario['speed'] = -10
        mario['mod_costum'].set_costum_jump(mario)


def go_x(mario, side):
    bloks = mario['grounds'].copy()
    if mario['id'] in bloks:
        bloks.remove(mario['id'])
    if side == 'right':
        sprite.move(mario['id'], 3, 0)
        if sprite.is_collide_all(mario['id'], bloks):
            sprite.move(mario['id'], -3, 0)
        mario['mod_costum'].look_right(mario, )

    elif side == 'left':
        sprite.move(mario['id'], -3, 0)
        if sprite.is_collide_all(mario['id'], bloks):
            sprite.move(mario['id'], 3, 0)
        mario['mod_costum'].look_left(mario, )
    mario['mod_costum'].animation_go(mario)
    mario['help'] = found_ground(mario, mario['grounds'])


def found_ground(mario, bloks):
    bloks = bloks.copy()
    if mario['id'] in bloks:
        bloks.remove(mario['id'])
    for r in bloks.copy():
        a = sprite.get_left(mario['id'])
        s = sprite.get_right(mario['id'])
        e = sprite.get_bottom(mario['id'])
        d = sprite.get_left(r)
        f = sprite.get_right(r)
        t = sprite.get_top(r)
        if s < d:
            # sprite.remove(r)
            bloks.remove(r)
        elif a > f:
            # sprite.remove(r)
            bloks.remove(r)
        elif e > t:
            # sprite.remove(r)
            bloks.remove(r)
    m = len(bloks)
    if m > 0:
        maxs = sprite.get_top(bloks[0])
        for r in bloks:
            t = sprite.get_top(r)
            if maxs > t:
                maxs = t
        return maxs
    else:
        return 620

# h=[54,56,23,567,987]
# maxs=h[0]
# for k in h:
#     if k>maxs:
#         maxs=k
# print(maxs)
