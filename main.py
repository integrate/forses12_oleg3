import wrap
from wrap import sprite
import mario

wrap.world.create_world(1337,758,0,25)
wrap.world.set_back_image('mario.png')

mario_1=mario.add_mario(300,309,1)
mario_2=mario.add_mario(600,390,4)
#mario.move_mario_y(mario_1)
#mario.move_mario_y(mario_2)

@wrap.always()
def move ():
    mario.move_mario_y(mario_1)
    mario.move_mario_y(mario_2)

#
#
# rf = 9807
# t = True
# v = [9, 67, 98, 7]
# for r in v:
#     print(r)
# ttt = v
# a = rf
# rf = rf + 1
# v.append(80)
# print(v[2])
# v[2] = v[2] + 1
#
# f = {'name': 'tolik', 'age': 15, 'ves': 45}
# print(f['ves'])
# f['age'] = f['age'] - 1
# f['rost'] = 155
# v.clear()
# v.append(f)
#
# f = {'name': 'marik', 'age': 15, 'ves': 59, 'rost': 170}
# v.append(f)
#
# f = {'name': 'narik', 'age': 14, 'ves': 42, 'rost': 140}
# v.append(f)
#
# for s in v:
#     s['date'] = 2022 - s['age']
#
# for y in v:
#     print(y['age'], y['name'])