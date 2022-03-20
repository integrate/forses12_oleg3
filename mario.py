import wrap
from wrap import sprite

import mario_costume


def add_mario(x, y, speed, path, costum, mod):
    id = sprite.add(path, x, y, costum)
    f = {'id': id, 'speed': speed, 'mod_costum': mod}
    return f


def move_mario_y(mario, ground):
    y = sprite.get_bottom(mario['id'])
    sprite.move(mario['id'], 0, mario['speed'])
    if y < ground:
        mario['speed'] += 1
        y = sprite.get_bottom(mario['id'])
    if y > ground:
        sprite.move_bottom_to(mario['id'], ground)
        mario['mod_costum'].set_costum_stand(mario)
        mario['speed']=0


def prizok(mario, ground):
    y = sprite.get_bottom(mario['id'])

    if y == ground:
        mario['speed'] = -10
        mario['mod_costum'].set_costum_jump(mario)



def go_x(mario, side):
    if side == 'right':
        sprite.move(mario['id'], 3, 0)
        mario['mod_costum'].look_right(mario,)

    elif side == 'left':
        sprite.move(mario['id'], -3, 0)
        mario['mod_costum'].look_left(mario,)
    mario['mod_costum'].animation_go(mario)

def found_ground(mario,bloks):
    bloks=bloks.copy()
    for r in bloks.copy():
        a=sprite.get_left(mario['id'])
        s=sprite.get_right(mario['id'])
        e=sprite.get_y(mario['id'])
        d=sprite.get_left(r)
        f=sprite.get_right(r)
        t=sprite.get_y(r)
        if s<d :
            # sprite.remove(r)
            bloks.remove(r)
        elif a>f:
            # sprite.remove(r)
            bloks.remove(r)
        elif e>t:
            # sprite.remove(r)
            bloks.remove(r)
    m=len(bloks)
    if m>0:
        maxs=sprite.get_y(bloks[0])
        for r in bloks:
            t = sprite.get_y(r)
            if maxs>t:
                maxs=t
        print(maxs)
    else:
        print(2090)

# h=[54,56,23,567,987]
# maxs=h[0]
# for k in h:
#     if k>maxs:
#         maxs=k
# print(maxs)
